from base_handler import *


class ReadMore(Handler):
    """Handler for viewing a post, including its comments and likes"""
    def get(self, post_id):
        post = Posts.by_id(int(post_id))

        if not post:
            # Post was not found
            self.error(404)
            return

        # Retrieve all comments on this post
        comments = Comments.all().filter(
            "post_id = ", int(post_id)).order('-created')

        if not self.user:
            action = 'like'
        else:
            # If the user has already liked the post,
            # then he is only allowed to unlike it
            action = 'like' if self.user.name not in post.likes else 'unlike'

        self.render("readmore.html",
                    post=post,
                    user=self.user,
                    action=action,
                    comments=comments)
