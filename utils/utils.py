import os
import re
import hashlib
import hmac
import random
from string import letters


def validate_user(username):
    """Checks whether the given username is well-formed.
    Returns an error message or empty string if there is no error."""
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

    if USER_RE.match(username):
        return ""
    return "That's not a valid username."


def validate_password(password):
    """Checks whether the given password is well-formed.
    Returns an error message or empty string if there is no error."""
    USER_PASS = re.compile(r"^.{3,20}$")

    if USER_PASS.match(password):
        return ""
    return "That wasn't a valid password."


def verify_password(password, verify):
    """Checks whether the given passwords match.
    Returns an error message or empty string if there is no error."""
    if password == verify:
        return ""
    return "Your passwords didn't match."


def validate_email(email):
    """Checks whether the given email address is well-formed.
    Returns an error message or empty string if there is no error."""
    USER_EMAIL = re.compile(r"^[\S]+@[\S]+.[\S]+$")

    if email == "" or USER_EMAIL.match(email):
        return ""
    return "That's not a valid email."

# Hashing functions for Cookies


def make_secure_val(val):
    secret = "inDlGelDgadazozoeaan"
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val


# Hashing user's passwords.
def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)


def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)
