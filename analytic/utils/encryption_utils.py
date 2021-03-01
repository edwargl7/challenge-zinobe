"""Encryption Utilities

https://www.geeksforgeeks.org/sha-in-python/
"""

import hashlib


def encrypt_with_sha1(text) -> str:
    """Encrypt text with SHA1 algorithm

    :param text: text to encrypt
    :type text: str

    :return: the equivalent hexadecimal value of the encrypted text
    whit SHA1
    """
    encrypted_text = hashlib.sha1(text.encode())
    return encrypted_text.hexdigest()
