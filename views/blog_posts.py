from base_handler import *


class BlogPosts(Handler):
    """Handler for the page that shows the collection of posts"""
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Posts ORDER BY created DESC")
        self.render("blogposts.html", posts=posts, user=self.user)
