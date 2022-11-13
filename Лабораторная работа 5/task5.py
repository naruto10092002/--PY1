from random import sample

ALPHABET = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"


def get_random_password(n=8) -> str:
    return ''.join(sample(ALPHABET, k=n))


print(get_random_password())
