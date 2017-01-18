from base_handler import *


class EditPost(Handler):
    """Handler for editing an existing post"""
    def get(self, post_id):
        """Returns html which allows the user to edit a post"""
        if not self.user:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")
        else:
            post = Posts.by_id(int(post_id))
            if post:
                author = post.username
                if author == self.user.name:
                    self.render("edit_post.html",
                                new_content=post.content,
                                post_id=int(post_id),
                                user=self.user)
                else:
                    error = "You are not authorized to edit this post."
                    posts = db.GqlQuery(
                        "SELECT * FROM Posts ORDER BY created DESC")

                    self.render("blogposts.html",
                                posts=posts,
                                user=self.user,
                                post_id=int(post_id),
                                error=error)
            else:
                # Post was not found
                self.error(404)
                return

    def post(self, post_id):
        """Attempts to edit a post"""
        post = Posts.by_id(int(post_id))

        if not post:
            # Post was not found
            self.error(404)
            return

        author = post.username
        if author != self.user.name:
            # Logged in user is not authorized to edit post
            self.error(403)
            return

        action = self.request.get("action")

        # Only save new content of the post if action is "save"
        if action == "save":
            post.content = self.request.get("edition")
            post.put()

        # Redirect the user to this post page
        self.redirect("/blog/%d" % int(post_id))
