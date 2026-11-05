# Synced

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Synced](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Rsync listing, download, and local flag read](assets/02-flag-retrieval.png)

## What I did

1. Listed the rsync daemon's available modules without supplying a username or password:

   ```bash
   rsync --list-only rsync://<target-ip>/
   ```

   The daemon exposed a module named `public`, described as an anonymous share. An rsync module is the named share that the daemon makes available to clients.

2. Listed the contents of that module without downloading anything:

   ```bash
   rsync --list-only rsync://<target-ip>/public/
   ```

   The listing showed `flag.txt` at the root of the share.

3. Copied that file into the current local directory and read it:

   ```bash
   rsync rsync://<target-ip>/public/flag.txt .
   cat flag.txt
   ```

4. Submitted the displayed flag to complete the lab.

The `--list-only` option enumerates available modules or files; the later `rsync` command performs the transfer. The flag value is not transcribed in this write-up.
