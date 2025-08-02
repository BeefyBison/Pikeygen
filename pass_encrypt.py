#!/usr/bin/python3
"""Runs a subprocess that passes in the password to clevis and returns the output."""
import subprocess

def encrypt_pass(password):
    """Encrypts a password with clevis if a tpm2 chip exists on the system."""
    encrypted_pass = "False"
    try:
        result = subprocess.run(
            ["clevis", "encrypt", "tpm2", "{}"],
            input=password.encode(),
            capture_output=True,
            check=True
        )
        encrypted_pass = result.stdout.decode().strip()
        print("Encrypted Text (JWE):", encrypted_pass)
    except subprocess.CalledProcessError as cpe:
        print(f"Clevis command failed with error: {cpe.stderr.decode()}")
    except FileNotFoundError:
        print("Clevis command not found. Please confirm Clevis is installed.")
    if encrypted_pass == "False":
        print("Clevis encryption failed. Likely due to missing TPM2 chip.")
    return encrypted_pass
