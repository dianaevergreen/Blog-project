from google.appengine.ext import db
from utils import *


class User(db.Model):
    """Model class for user"""
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        """Returns the user object with the given id, if it exists"""
        return cls.get_by_id(uid)

    @classmethod
    def by_name(cls, name):
        """Returns the user object with the given name, if it exists"""
        u = cls.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email=None):
        """Returns the newly registered user object"""
        pw_hash = make_pw_hash(name, pw)
        return cls(name=name,
                   pw_hash=pw_hash,
                   email=email)

    @classmethod
    def login(cls, name, pw):
        """Attempts to authenticate a user using name and password.
        Returns the user object, if it exists
        and was successfully authenticated.
        """
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u
