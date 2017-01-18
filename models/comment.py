from google.appengine.ext import db


class Comments(db.Model):
    """Model class for comments"""
    username = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    post_id = db.IntegerProperty(required=True)

    @classmethod
    def by_id(cls, comment_id):
        """Returns the comment object with the given id, if it exists"""
        return cls.get_by_id(comment_id)
