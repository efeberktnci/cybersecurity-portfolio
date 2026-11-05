# Mongod

![Platform: Hack The Box](https://img.shields.io/badge/Platform-Hack%20The%20Box-9FEF00?style=for-the-badge) ![Type: Starting Point](https://img.shields.io/badge/Type-Starting%20Point-3B5BDB?style=for-the-badge) ![Difficulty: Very Easy](https://img.shields.io/badge/Difficulty-Very%20Easy-2F9E44?style=for-the-badge) ![OS: Linux](https://img.shields.io/badge/OS-Linux-495057?style=for-the-badge) ![Status: Solved](https://img.shields.io/badge/Status-Solved-2F9E44?style=for-the-badge)

Lab link: [Mongod](https://app.hackthebox.com/starting-point)

## Completion proof

![Completion proof](assets/01-completion-proof.png)

## Flag retrieval

![MongoDB database, collection, and flag query](assets/02-flag-retrieval.png)

## What I did

1. Downloaded and extracted the MongoDB Shell 2.3.2 archive from MongoDB's download server. This version connected successfully to the lab's MongoDB 3.6.8 server.
2. Connected to the target's MongoDB service on TCP port `27017`:

   ```bash
   ./mongosh-2.3.2-linux-x64/bin/mongosh mongodb://<target-ip>:27017
   ```

3. Ran `show dbs` and found a database named `sensitive_information`.
4. Selected it with `use sensitive_information`, then ran `show collections` and found the `flag` collection.
5. Ran `db.flag.find()` to display its document, read the `flag` field, and submitted that value to complete the lab.

The server warned that database access control was disabled; the connection therefore did not require credentials. The flag value is not transcribed in this write-up.
