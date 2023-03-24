
import random
import hashlib

SALT_LENGTH = 10
SALT_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def create_salt():
    """Create a salt for hashing"""
    return "".join(random.choice(SALT_CHARS) for _ in range(SALT_LENGTH))   

def hash(password):
    salt = create_salt()
    salted_password = password + salt
    """Hash a password for storing."""
    return hashlib.sha512(salted_password.encode()).hexdigest(), salt

def verify(hashed_password, password):
    """Verify a stored password against one provided by user"""
    salt = hashed_password[1]
    salted_password = password + salt
    return hashed_password[0] == hashlib.sha512(salted_password.encode()).hexdigest()


