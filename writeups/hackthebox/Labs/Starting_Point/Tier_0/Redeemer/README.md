# Redeemer

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Redeemer](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![Flag retrieval in Redis](assets/02-flag-retrieval.png)

## What I did

1. Scanned the full TCP port range from Pwnbox with `nmap -p- <target-ip>` and found Redis on `6379/tcp`.
2. Connected to the service with `redis-cli -h <target-ip> -p 6379`.
3. Checked Redis information and saw `db0:keys=4` in the keyspace section. This showed that database 0 contained four keys, so I selected it with `SELECT 0`.
4. Used `KEYS *` to list those four keys, including `flag`.
5. Read the value with `GET flag` and submitted it to complete the lab.

The flag value is intentionally omitted from this write-up.
