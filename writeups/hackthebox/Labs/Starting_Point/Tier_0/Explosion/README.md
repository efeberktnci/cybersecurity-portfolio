# Explosion

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Windows](https://img.shields.io/badge/OS-Windows-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Explosion](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Flag opened on the remote desktop](assets/02-flag-retrieval.png)

## What I did

1. Connected to the Starting Point target from Pwnbox and identified the Remote Desktop service on `3389/tcp`.
2. Used `xfreerdp /v:<target-ip> /u:Administrator` to start an RDP session. The `/v:` option specifies the target host and `/u:` supplies the Windows username.
3. Left the password blank and reached the target's Windows desktop.
4. Opened the `flag` text file on the desktop and submitted its value to complete the lab.

The flag value is not transcribed in this write-up.
