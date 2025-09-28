# This code will create user in Linux.

import os
import subprocess

def create_user(username)->int:
    try:
        subprocess.run(["sudo","useradd",username])
        print(f"User {username} is added.")
        return 0
    except:
        print("Error while creatin user")
        return -1

username = input("Enter username : ")
create_user(username=username)
