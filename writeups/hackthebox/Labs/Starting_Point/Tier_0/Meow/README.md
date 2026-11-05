# Meow

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Meow](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Flag retrieval terminal](assets/02-flag-retrieval.png)

## What I did

1. Scanned the authorized target to identify its reachable service.
2. Found Telnet exposed on port `23/tcp`.
3. Connected to the intentionally vulnerable lab service using the credentials indicated by the exercise.
4. Listed the root home directory and read the flag file to complete the machine.

The flag value is intentionally omitted from this write-up.
