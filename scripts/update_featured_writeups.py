"""Show the three most recently added write-ups for each platform."""

from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "writeups/hackthebox/Labs"
STARTING_POINT = LABS / "Starting_Point"
TIERS = {
    "Tier_0": ("Tier 0 - Foundations", 0),
    "Tier_1": ("Tier 1 - Fundamental Exploitation", 1),
}
README = ROOT / "README.md"


def added_order():
    """Return creation order from Git, preserving it across folder moves."""
    output = subprocess.run(
        ["git", "log", "--reverse", "--diff-filter=AR", "-M", "--format=", "--name-status", "--", "writeups"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    order = {}
    for line in output.splitlines():
        fields = line.split("\t")
        if len(fields) == 2 and fields[0] == "A" and fields[1].startswith("writeups/"):
            order[fields[1]] = len(order)
        elif len(fields) == 3 and fields[0].startswith("R") and fields[1] in order:
            order[fields[2]] = order.pop(fields[1])
    return order


def candidates(platform):
    base = ROOT / "writeups" / platform
    if platform == "hackthebox":
        return [p for tier in TIERS for p in (STARTING_POINT / tier).glob("*/README.md")]
    if platform == "letsdefend":
        return [p for p in base.rglob("README.md") if p.parent.name != "SOC_Fundamentals" and p.parent != base]
    return [
        p for p in base.rglob("*.md")
        if p.name != "README.md" and not p.name.startswith("00-notes")
    ]


def title(path):
    if path.parent.parent in [STARTING_POINT / tier for tier in TIERS]:
        return path.parent.name
    match = re.search(r"^#\s+(.+)$", path.read_text(encoding="utf-8", errors="replace"), re.M)
    value = match.group(1).strip() if match else path.stem.replace("_", " ")
    return re.sub(r"^Lab:\s*", "", value)


def markdown_link(path, prefix=""):
    relative = path.relative_to(ROOT).as_posix()
    if path.name == "README.md":
        relative = relative.removesuffix("README.md")
    label = title(path).replace("|", "\\|").replace("]", "\\]")
    return f"[{label}]({prefix}{relative})"


def replace_platform_row(content, platform, links):
    lines = content.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if f"**{platform}**" in line and line.startswith("| ")]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {platform} table row")
    index = matches[0]
    cells = lines[index].rstrip("\r\n").split(" | ")
    if len(cells) != 3 or not cells[2].endswith(" |"):
        raise RuntimeError(f"Unexpected table format for {platform}")
    cells[2] = " · ".join(links) + " |"
    lines[index] = " | ".join(cells) + "\n"
    return "".join(lines)


def write_if_changed(path, content):
    if path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"Updated {path.relative_to(ROOT)}")


def main():
    order = added_order()
    latest = {}
    for directory, name in (
        ("tryhackme", "TryHackMe"),
        ("hackthebox", "Hack The Box"),
        ("letsdefend", "LetsDefend"),
        ("portswigger", "PortSwigger Web Security Academy"),
    ):
        paths = [p for p in candidates(directory) if p.relative_to(ROOT).as_posix() in order]
        paths.sort(key=lambda p: -order[p.relative_to(ROOT).as_posix()])
        latest[name] = paths

    content = README.read_text(encoding="utf-8")
    for name, paths in latest.items():
        content = replace_platform_row(content, name, [markdown_link(p) for p in paths[:3]])
    write_if_changed(README, content)

    labs = latest["Hack The Box"]
    index = ROOT / "writeups/hackthebox/README.md"
    content = index.read_text(encoding="utf-8")
    replacement = "  - [Starting Point](Labs/Starting_Point/)\n"
    for tier, (label, _) in TIERS.items():
        tier_paths = [p for p in labs if p.parent.parent.name == tier]
        replacement += f"    - [{label}](Labs/Starting_Point/{tier}/)\n"
        replacement += "".join(
            f"      - [{p.parent.name}](Labs/Starting_Point/{tier}/{p.parent.name}/)\n" for p in tier_paths
        )
    content, count = re.subn(
        r"(?<=- \[Labs\]\(Labs/\)\n)(?:  - \[[^\n]+\n|    - \[[^\n]+\n)*",
        lambda _: replacement, content, count=1,
    )
    if count != 1:
        raise RuntimeError("Could not find HTB Labs index")
    write_if_changed(index, content)

    index = LABS / "README.md"
    content = index.read_text(encoding="utf-8")
    replacement = "- [Starting Point](Starting_Point/)\n"
    for tier, (label, _) in TIERS.items():
        replacement += f"  - [{label}](Starting_Point/{tier}/)\n"
    content, count = re.subn(
        r"(?<=# Hack The Box Labs\n\n)(?:- \[[^\n]+\n)*",
        lambda _: replacement, content, count=1,
    )
    if count != 1:
        raise RuntimeError("Could not find HTB Labs README")
    write_if_changed(index, content)

    index = STARTING_POINT / "README.md"
    content = index.read_text(encoding="utf-8")
    replacement = ""
    for tier, (label, _) in TIERS.items():
        tier_paths = [p for p in labs if p.parent.parent.name == tier]
        replacement += f"- [{label}]({tier}/)\n"
        replacement += "".join(f"  - [{p.parent.name}]({tier}/{p.parent.name}/)\n" for p in tier_paths)
    content, count = re.subn(
        r"(?<=# Hack The Box Starting Point\n\n)(?:(?:- |  - )\[[^\n]+\n)*",
        lambda _: replacement, content, count=1,
    )
    if count != 1:
        raise RuntimeError("Could not find HTB Starting Point README")
    write_if_changed(index, content)


if __name__ == "__main__":
    main()
