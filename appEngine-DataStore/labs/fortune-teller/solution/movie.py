from google.appengine.ext import ndb


class Movie(ndb.Model):
    

    title = ndb.StringProperty(required=True)
    media_type = ndb.StringProperty(required=True, default ='Movie')
    runtime = ndb.StringProperty(required=False)
    rating = ndb.StringProperty(required=False)

    def __init__(self,mov_title,runtime,user_rating):
        self.title = mov_title
        self.runtime_mins = runtime_mins
        self.rating = user_rating
