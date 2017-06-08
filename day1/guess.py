#!/usr/bin/env python3
# coding:utf-8

import os
import getpass

PROGRAM_ROOT = os.path.dirname(os.path.abspath(__file__))
LOCK_FILE = os.path.join(PROGRAM_ROOT,'user.lock')
USERS_FILE = os.path.join(PROGRAM_ROOT,'users.data')

def is_lock_name(name):
    with open(LOCK_FILE,'r') as f:
        for line in f.readlines():
            if line.strip() == name:
                return True
            else:
                return False

def set_lock_name(name):
    with open(LOCK_FILE,'w') as f:
        f.writelines(name)

def verify_login(username,password):
    with open(USERS_FILE,'r') as f:
        for line in f.readlines():
            user_data = line.strip().split('---')
            print(user_data[0],user_data[1])
            if user_data[0]==username and user_data[1] == password:
                return True
        else:
            return False


login_log = {}
login_count = 0
while True:
    username = input('Input your username:')
    password = getpass.getpass('Input your password:')

    if is_lock_name(username):
        print('This user is locked.Try another one')
        continue

    if verify_login(username,password):
        print('Hi {name}, Welcome back!'.format(name=username))
        break
    else:
        print('Username or Password wrong!')
        if username in login_log:
            login_log[username] += 1
        else:
            login_log[username] = 1

    if login_log[username] >= 3:
        print('You have been try too many times!')
        set_lock_name(username)

    login_count += 1
    if login_count >= 3:
        choice = input('Still wanna try？(Y)es or (N)o:')
        if choice == 'Y':
            login_count = 0
        elif choice == 'N':
            break