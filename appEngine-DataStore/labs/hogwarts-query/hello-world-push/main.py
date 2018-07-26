import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Brooke's Online Portal")

app = webapp2.WSGIApplication([
    ('/hello-world', MainHandler)

], debug=True)
