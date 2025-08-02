#!/usr/bin/python3
"""Creates a string of characters and a salt for password use based on hostname."""
from functools import reduce
import argparse
import random
import re
import secrets
import string
import sys

import pass_encrypt

DEFAULT_HOSTNAME = ""

parser=argparse.ArgumentParser(description="Hostname based password generator - args are optional")
parser.add_argument("passed_in_hostname", nargs='?', default=DEFAULT_HOSTNAME)
parser.add_argument("--length", type=int, nargs='?', default=random.randrange(16,20))
args=parser.parse_args()

def create_random_string():
    """Creates a random string with at least 1 lowercase character, 1 uppercase character,
    and at least 3 digits for use in other functions."""
    valid_spec_characters = "@#$%^&*()_+=-"
    characters = string.ascii_letters + string.digits + valid_spec_characters
    while True:
        created_string = ''.join(secrets.choice(characters) for i in range(args.length))
        if (any(c.islower() for c in created_string) <=3
                and any(c.isupper() for c in created_string) <=3
                and any(c in valid_spec_characters for c in created_string) <=3
                and sum(c.isdigit() for c in created_string) >=3
                and not bool(reduce(lambda x, y: (x is not y) and x and y, created_string))):
            break
    return str(created_string)

def remove_number(hostname):
    """Removes numbers from given hostname."""
    s = hostname
    result = ''.join([i for i in s if not i.isdigit()])
    return result

def remove_special(hostname):
    """Removes special characters from a given hostname."""
    s = hostname
    result = ''.join([i for i in s if i.isalnum()])
    return result

def put_back_number(salt, hostname):
    """Takes a hostname and places the number back on the salt."""
    s = hostname
    first_number = next((char for char in s if char.isdigit()), None)
    if first_number is None:
        first_number = 1 # Sets a default if none exist
        first_number = str(first_number)
    s = remove_number(s)
    pre_result = ''.join([i for i in s if i.isdigit()])
    pre_result = pre_result + first_number
    result = salt + pre_result
    return result

def calculate_salt(hostname):
    """Calculates a salt to add to a created password depending on a given hostname.
     1st row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
     2nd row = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
     3rd row = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    """
    x = ""
    y = ""
    hostname_edit = remove_number(hostname)
    hostname_edit = remove_special(hostname_edit)
    keyboard = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
                'z', 'x', 'c', 'v', 'b', 'n', 'm']
    for letter in keyboard:
        t = keyboard.index(letter)
    # Left side of keyboard
        if hostname_edit.startswith(letter):
            try:
                x = keyboard[t-1]
                if letter == 'a':
                    x = 'l'
                elif letter == 'z':
                    x = 'm'
            # Ensures the list wraps around
            except IndexError:
                if letter == 'q':
                    x = 'p'
    # Right side of Keyboard
        if hostname_edit.endswith(letter):
            try:
                y = keyboard[t+1]
                if letter == 'p':
                    y = 'q'
                elif letter == 'l':
                    y = 'a'
            # Ensures the list wraps around
            except IndexError:
                if letter == 'm':
                    y = 'z'
    pre_salt = x + y
    salt = put_back_number(pre_salt, hostname)
    salt = salt + salt
    return salt

def main(hostname):
    """Executes random string and salt, and combines them."""
    first_half = create_random_string()
    second_half = calculate_salt(hostname)
    password = first_half + second_half
    print(first_half)
    pass_encrypt.encrypt_pass(password)
    return password

### TO DO: Add requirement for no more than 4 consecutive characters of the same type

if __name__ == "__main__":
    try:
        if args.passed_in_hostname!="":
            print(main(args.passed_in_hostname))
        else:
            print(main(DEFAULT_HOSTNAME))
    except SyntaxError as se:
        print("A syntax error has occurred:", {se})
        sys.exit(1)
    except ValueError as ve:
        print("A value error has occurred:", {ve})
        sys.exit(1)
    except TypeError as te:
        print("A type error has occurred:", {te})
        sys.exit(1)
    except SystemError as syse:
        print("A system error has occurred:", {syse})
        sys.exit(1)
    except RuntimeError as re:
        print("A runtime error has occurred:", {re})
        sys.exit(1)
    except KeyboardInterrupt as ke:
        print("User interrupt received:", {ke})
        sys.exit(1)
    except IndexError as ie:
        print("Index error at:", {ie})
        sys.exit(1)
