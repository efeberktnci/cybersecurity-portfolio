# Dancing

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Windows](https://img.shields.io/badge/OS-Windows-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Dancing](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Flag retrieval on Pwnbox](assets/02-flag-retrieval.png)

## What I did

1. Connected to the Dancing target from Pwnbox and used `smbclient -L <target-ip>` to list its SMB shares.
2. Found four shares: `ADMIN$`, `C$`, `IPC$`, and `WorkShares`. The first two returned access denied; `IPC$` did not provide a browsable file listing.
3. Connected to the accessible file share with `smbclient //<target-ip>/WorkShares -N`.
4. Listed the share and found the `Amy.J` and `James.P` directories. Opened `James.P` and found `flag.txt`.
5. Downloaded the file with SMB client's `get` command, opened the local copy, and submitted the flag to complete the lab.

The flag value is intentionally omitted from this write-up.
