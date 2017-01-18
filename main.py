import webapp2
from views import *


app = webapp2.WSGIApplication([('/blog', BlogPosts),
                               ('/', BlogPosts),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Signup),
                               ('/welcome', Welcome),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/delete/([0-9]+)', DeletePost),
                               ('/blog/edit/([0-9]+)', EditPost),
                               ('/blog/readmore/([0-9]+)', ReadMore),
                               ('/blog/like/([0-9]+)', Likes),
                               ('/blog/post/comment/([0-9]+)', Comment),
                               ('/blog/comment/edit/([0-9]+)', EditComment),
                               ('/blog/comment/delete/([0-9]+)', DeleteComment)
                               ],
                              debug=True)
