from base_handler import *


class Comment(Handler):
    """Handler for composing a new comment"""
    def get(self, post_id):
        """Returns html which allows the user to enter a comment"""
        if self.user:
            self.render("comment.html", user=self.user, post_id=post_id)
        else:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")

    def post(self, post_id):
        """Attempts to add a comment to a given post"""
        if self.user:
            content = self.request.get("content")
            username = self.user.name

            if content:
                comment = Comments(content=content,
                                   username=username,
                                   post_id=int(post_id))
                comment.put()

                # Successfully added comment. Redirect user to the post page.
                self.redirect("/blog/readmore/%s" % post_id)
            else:
                error = "Subject and content, please!"
                self.render("comment.html",
                            content=content,
                            error=error,
                            user=self.user)
        else:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")
