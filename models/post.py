from google.appengine.ext import db


class Posts(db.Model):
    """Model class for posts"""
    username = db.StringProperty(required=True)
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    likes = db.ListProperty(str)  # A list of usernames who have liked the post

    @classmethod
    def by_id(cls, post_id):
        """Returns the post object with the given id, if it exists"""
        return cls.get_by_id(post_id)
