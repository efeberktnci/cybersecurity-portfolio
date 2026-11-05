# Appointment

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Appointment](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Login page

![Appointment login page](assets/02-login-page.png)

## Flag retrieval

![Flag displayed after login](assets/03-flag-retrieval.png)

## What I did

1. Opened the target's web page and found a login form.
2. The task identified SQL injection and explained that `#` comments out the rest of a MySQL line. I entered `admin'#` as the username and any value as the password. The apostrophe closes the username string and `#` comments out the password condition in the vulnerable query.
3. The login succeeded and the page displayed the flag. I submitted it to complete the lab.

This write-up records the successful lab path and does not transcribe the flag value.
