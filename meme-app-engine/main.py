# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from google.appengine.api import urlfetch
import json
import urllib
import random


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        # self.response.write("""Brooke is the coolest ever person
        # and is definetly cooler than you!""")
        #
        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                # self.response.write(type(result.content))
                random_text = ['this is a meme', 'eff you bro','goodbye bih', 'okurr','poop scoop', 'go away']
                json_dict=json.loads(result.content)
                # picture_url = (json_dict['data']['memes'][0]['url'])
                # self.response.write('<img src="{pic}"/>'.format(pic=picture_url))
                random_meme = random.choice(json_dict['data']['memes'])['id']
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
        'template_id':random_meme,
        'username': 'brookeokay',
        'password': 'brookeokay',
        'text0': random.choice(random_text),
        'text1':random.choice(random_text)
        }
        result = urlfetch.fetch(
            url=caption_url,
            payload=urllib.urlencode(caption_dict),
            method=urlfetch.POST)
        new-meme-dict = json.loads(result.content)
        picture_url = new-meme-dict['data']['url']
        self.response.write('<img src="{pic}"/>'.format(pic = picture_url))



app = webapp2.WSGIApplication([
    ('/', MainPage),


], debug=True)
