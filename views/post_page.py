from base_handler import *


class PostPage(Handler):
    """Handler for viewing a newly created post"""
    def get(self, post_id):
        post = Posts.by_id(int(post_id))

        if not post:
            self.error(404)
            return

        self.render("postpage.html",
                    post=post,
                    user=self.user)
