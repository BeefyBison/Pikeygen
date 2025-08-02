# Pikeygen

Pikeygen is a python library for automatically generating random passwords and salting them.
This is intended to be used with Ansible playbooks in order to automatically set passwords for users based on hostname.
It also has Clevis capability if a TPM2 chip exists on the system.

## Version

0.3 
- August 2025
- Ready for testing. Bugs may exist, or some planned functionality may not be implemented yet.

## Installation

Simply place the pikeygen files in the location you want it installed.
Switch to that directory.

## Usage
A hostname is optional, but not required. The salt will be added to the end of the password based on the hostname given.

Absolute or relative path is fine.

```
Intended to be executed from an ansible ready host.

When using with ansible: sudo ansible-playbook pikeygen_play.yml
Prompts will be a guide for execution of the password generator.
The prompts will hide the base password, and the password will be set to the base password + the
generated password + the double tap salt. The double tap is added to the end of the password that
is known in advance.

usage: pikeygen.py [-h] [ [HOSTNAME]] [--length [LENGTH]]

Hostname based password generator - args are optional

options:
  -h, --help            show this help message and exit
  [HOSTNAME]
  --length [LENGTH]
```

```python
python3 pikeygen.py

# returns a randomly generated password with a salt.

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)