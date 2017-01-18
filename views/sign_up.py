from base_handler import *


class Signup(Handler):
    """Handler for the Sign Up process"""
    def get(self):
        """Takes a user to the welcome page if successfully authenticated,
        or to the sign up page otherwise."""
        if self.user:
            self.redirect('/welcome')
        else:
            self.render("signup.html")

    def post(self):
        """Attempts to sign a new user up"""
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        # Validate user input
        user_error = validate_user(username)
        password_error = validate_password(password)
        verification_error = verify_password(password, verify)
        email_error = validate_email(email)

        if user_error or password_error or verification_error or email_error:
            self.render("signup.html",
                        username=username,
                        password=password,
                        verify=verify,
                        email=email,
                        user_error=user_error,
                        password_error=password_error,
                        verification_error=verification_error,
                        email_error=email_error)

        else:
            # No errors in user input
            u = User.by_name(username)
            if u:
                # User already exists
                error_message = "That user already exists"
                self.render("signup.html",
                            user_error=error_message)
            else:
                # Create a new user
                u = User.register(username, password, email)
                u.put()
                # Save auth cookies and redirect user to welcome page
                self.login(u)
                self.redirect("/welcome")
