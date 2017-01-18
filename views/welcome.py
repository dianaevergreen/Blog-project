from base_handler import *


class Welcome(Handler):
    """Handler for the welcome page"""
    def get(self):
        """Takes a user to the welcome page if authenticated,
        or to the sign up page otherwise."""
        if self.user:
            self.render("welcome.html",
                        user=self.user,
                        username=self.user.name)
        else:
            self.redirect("/signup")
