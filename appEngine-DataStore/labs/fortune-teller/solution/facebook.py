from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    image = ndb.StringProperty(required=False, default='ghost')
    post = ndb.StringProperty(required=False)
    friends = ndb.StringProperty(required=False)

    # def __init__(self,user_email, user_password,account_name,profile_picture,user_post,user_friends):
    #     self.email = user_email
    #     self.password = user_password
    #     self.name = account_name
    #     self.image = profile_picture
    #     self.post = user_post
    #     self.friends = user_friends

class Post(ndb.Model):

    uploads = ndb.StringProperty(required=False)
    likes = ndb.StringProperty(required=False)
    shares = ndb.StringProperty(required=False)
    views = ndb.StringProperty(required=False)


    # def __init__(self,user_uploads, user_likes,user_shares,user_views):
    #
    #     self.uploads = user_uploads
    #     self.likes = user_likes
    #     self.shares = user_shares
    #     self.views = user_views

    
