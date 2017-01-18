from base_handler import *


class DeletePost(Handler):
    """Handler for deleting a post"""
    def post(self, post_id):
        """Attempts to delete a given post"""
        if not self.user:
            # Redirects the user to the login screen if not authenticated
            self.redirect("/login")
        else:
            post = Posts.by_id(int(post_id))
            if post:
                author = post.username
                if author == self.user.name:
                    post.delete()
                    # Retrieve all posts except the one we've just deleted
                    posts = Posts.all().filter("__key__ != ", post.key())
                    self.render("blogposts.html",
                                posts=posts,
                                user=self.user)
                    return
                else:
                    error = "You are not authorized to delete this post."
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
