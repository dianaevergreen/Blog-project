from base_handler import *


class Logout(Handler):
    """Handler for the sign out process"""
    def get(self):
        """Logs the user out"""
        # Removes auth cookie
        self.logout()
        # Redirects user to sign up page
        self.redirect('/signup')
