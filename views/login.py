from base_handler import *


class Login(Handler):
    """Handler for the sign in process"""
    def get(self):
        """Takes a user to the welcome page if successfully authenticated,
        or to the login page otherwise."""
        if self.user:
            self.redirect('/welcome')
        else:
            self.render("login.html")

    def post(self):
        """Attempts to log a user in using username and password"""
        username = self.request.get('username')
        password = self.request.get('password')

        # Trying to authenticate the user
        u = User.login(username, password)
        if u:
            # Successfully authenticated
            # Save auth cookie and redirect user to the welcome page
            self.login(u)
            self.redirect('/welcome')
        else:
            error_message = 'Invalid login'
            self.render('login.html',
                        username=username,
                        error=error_message)
