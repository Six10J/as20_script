#!/usr/bin/env python3
# -*- -*- -*-

import random
import hashlib

def generate_random_number_string():

    if PWD_LGT >= 9:
        return ''.join(random.choice("0123456789") for X in range(PWD_LGT))

    else:
        return ''.join(random.choice("0123456789") for X in range(9))

def md5_hash(text):

    return hashlib.md5(text.encode()).hexdigest()

def main():

    for i in range(NO_PASS):

        password = generate_random_number_string()

        hash_value = md5_hash(password)

        print(hash_value)

        #print(f"{i+1:2d}. Lösenord: {password}  →  MD5: {hash_value}")


PWD_LGT = 10
NO_PASS = 10

if __name__ == "__main__":
    main()
