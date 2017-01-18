from base_handler import *


class DeleteComment(Handler):
    """Handler for deleting a comment"""
    def post(self, comment_id):
        """Attempts to delete a given comment"""
        if not self.user:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")
        else:
            comment = Comments.by_id(int(comment_id))
            if comment:
                post_id = comment.post_id
                post = Posts.by_id(post_id)

                # If the user has already liked the post,
                # then he is only allowed to unlike it
                action = 'like' if self.user.name \
                    not in post.likes else 'unlike'

                author = comment.username

                if author == self.user.name:
                    # Retrieves all comments from this post,
                    # except the one we're supposed to delete
                    comments = Comments.all() \
                        .filter("post_id = ", int(post_id)) \
                        .filter("__key__ != ", comment.key())

                    comment.delete()
                    error = ""
                else:
                    error = "You are not authorized to delete this comment."

                    # Retrieves all comments from this post
                    comments = Comments.all() \
                        .filter("post_id = ", int(post_id)).order('-created')

                self.render("readmore.html",
                            post=post,
                            comment_id=int(comment_id),
                            user=self.user,
                            action=action,
                            comments=comments,
                            error=error)
            else:
                # Comment was not found
                self.error(404)
                return
