from base_handler import *


class Likes(Handler):
    """Handler for liking/unliking a post"""
    def get(self, post_id):
        self.redirect("/blog/readmore/%s" % post_id)

    def post(self, post_id):
        """Attempts to like/unlike a post"""
        post = Posts.by_id(int(post_id))
        if not post:
            self.error(404)
            return

        # This will be either 'like' or 'unlike'
        action = self.request.get("action")

        if not self.user:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")
        else:
            comments = Comments.all().filter(
                "post_id = ", int(post_id)).order('-created')
            # Assuming action is 'like'
            # We only need to update the post's likes
            # if the user didn't like it already
            needs_update = self.user.name not in post.likes
            # The operation to perform on the list of likes
            operation = post.likes.append
            opposite_action = 'like' if action == 'unlike' else 'unlike'

            if action == 'unlike':
                # Flip the needs_update flag,
                # as it was assuming action to be like
                needs_update = not needs_update
                # Flip the operation as well
                operation = post.likes.remove

            if self.user.name != post.username:
                if needs_update:
                    operation(self.user.name)
                    post.put()

                    # Success!
                    like_message = "You've %sd this post" % action
                else:
                    like_message = "You already %sd this post" % action
            else:
                like_message = "You can't %s your own post" % action
                self.render("readmore.html",
                            post=post,
                            comments=comments,
                            user=self.user,
                            like_message=like_message,
                            action=action)
                return

            self.render("readmore.html",
                        post=post,
                        comments=comments,
                        user=self.user,
                        like_message=like_message,
                        # When you've successfully liked a post,
                        # then you can only unlike it and viceversa
                        action=opposite_action)
