import random
import string


def rand_slug():
    return ''.join(random.choice(string.digits) for _ in range(6))
