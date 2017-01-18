from base_handler import *


class EditComment(Handler):
    """Handler for editing an existing comment"""
    def get(self, comment_id):
        """Returns html which allows the user to edit a comment"""
        if not self.user:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")
        else:
            comment = Comments.by_id(int(comment_id))
            if comment:
                author = comment.username
                if author == self.user.name:
                    self.render("edit_comment.html",
                                new_content=comment.content,
                                user=self.user,
                                comment_id=comment_id)
                else:
                    error = "You are not authorized to edit this comment."
                    post_id = comment.post_id
                    post = Posts.by_id(post_id)
                    comments = Comments.all() \
                        .filter("post_id = ", int(post_id)).order('-created')

                    # If the user has already liked the post,
                    # then he is only allowed to unlike it
                    action = 'like' if self.user.name \
                        not in post.likes else 'unlike'

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

    def post(self, comment_id):
        """Attempts to edit a comment"""
        comment = Comments.by_id(int(comment_id))

        if not comment:
            # Comment was not found
            self.error(404)
            return

        author = comment.username
        if author != self.user.name:
            # Logged in user is not authorized to edit comment
            self.error(403)
            return

        action = self.request.get("action")

        # Only save new content of the comment if action is "save"
        if action == "save":
            comment.content = self.request.get("edition")
            comment.put()

        # Redirect the user to this comment parent post page
        self.redirect("/blog/readmore/%d" % comment.post_id)
