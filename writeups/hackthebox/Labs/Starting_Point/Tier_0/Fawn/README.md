# Fawn

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Fawn](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Flag retrieval terminal](assets/02-flag-retrieval.png)

## What I did

1. Connected to the Starting Point lab through Pwnbox and scanned the authorized target.
2. Identified FTP on port `21/tcp`, with the server reporting `vsFTPd 3.0.3`.
3. Connected to the target with the FTP client.
4. Listed the remote directory and downloaded `flag.txt` with `get flag.txt`.
5. Left the FTP client and opened the downloaded `flag.txt` file to complete the machine.

The flag value is intentionally omitted from this write-up.
