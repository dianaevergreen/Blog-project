from base_handler import *


class NewPost(Handler):
    """Handler for composing a new post"""
    def get(self):
        """Returns html which allows the user to compose a post"""
        if self.user:
            self.render("newpost.html",
                        user=self.user)
        else:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")

    def post(self):
        """Attempts to create a post"""
        if self.user:
            subject = self.request.get("subject")
            content = self.request.get("content")
            username = self.user.name

            if subject and content:
                post = Posts(subject=subject,
                             content=content,
                             username=username)
                post.put()
                # Redirect the user to the newly created post
                self.redirect("/blog/%s" % str(post.key().id()))
            else:
                error = "Subject and content, please!"
                self.render("newpost.html",
                            user=self.user,
                            subject=subject,
                            content=content,
                            error=error)
        else:
            self.redirect("/login")
