# Preignition

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Preignition](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Flag displayed in the web page](assets/02-flag-retrieval.png)

## What I did

1. Connected to the target from Pwnbox and identified an HTTP service on `80/tcp`, served by `nginx 1.14.2`.
2. Enumerated web paths with `gobuster dir`, using the target URL and the local `/usr/share/wordlists/dirb/common.txt` wordlist.
3. Found `/admin.php` with HTTP status `200`. The chosen wordlist found the PHP page without adding a separate file-extension option.
4. Opened the discovered page in a browser and signed in to the Admin Console.
5. Read the flag displayed on the resulting page and submitted it to complete the lab.

The flag value is not transcribed in this write-up.
