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
import logging
import jinja2


template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)


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
                random_text = ['this is a meme', 'i Am sMaRt','goodbye bih', 'okurr','poop scoop', 'go away']
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
        new_meme_dict = json.loads(result.content)
        picture_url = new_meme_dict['data']['url']
        # self.response.write('<img src="{pic}"/>'.format(pic = picture_url))


class MemeType(webapp2.RequestHandler):
    def get(self):
        # Get all of the memes
        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                json_dict=json.loads(result.content)
                all_meme = json_dict['data']['memes']
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')


        # Make a dictionary
        meme_dicts = {}



        # Put all the memes in the dictiony where the key is the id and
        # the value is the id
        for meme in all_meme:
            meme_dicts['id']='name'

        self.response.write("Let's make a meme!")
        template = template_env.get_template('templates/home.html')
        data = {'img_src': 'https://i.imgflip.com/1otk96.jpg'}
        self.response.write(template.render(data))


class MemeResults(webapp2.RequestHandler):
    def post(self):
        meme_type = self.request.get('meme-type')
        textz = 'You clicked Winner and ofc winners are basketball players so...'
        textz2='Hey there!'
        template_id=''

        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                # self.response.write(type(result.content))

                json_dict=json.loads(result.content)
                # picture_url = (json_dict['data']['memes'][0]['url'])
                # self.response.write('<img src="{pic}"/>'.format(pic=picture_url))
                random_meme = random.choice(json_dict['data']['memes'])['id']
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        if meme_type == 'sports':
            textw= ['woo','booyahhh']
            textw2=['hee', 'awww yiissssss']
            textz=random.choice(textw)
            textz2=random.choice(textw2)
        #     self.response.write(textz);
        #     picz = 'https://www.spalding.com/dw/image/v2/ABAH_PRD/on/demandware.static/-/Sites-masterCatalog_SPALDING/default/dw10a8f40a/images/hi-res/Spalding-Digital-Assets_15520.jpg?sw=318&sh=395&sm=cut'
        else:

            textl=['Loser','sucks to suck','sorry bro']
            textl2=['Lol', 'hahahah','wowowowow']
            textz=random.choice(textl)
            textz2=random.choice(textl2)


        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
        'template_id': random_meme,
        'username': 'brookeokay',
        'password': 'brookeokay',
        'text0': textz,
        'text1': textz2
        }
        result = urlfetch.fetch(
            url=caption_url,
            payload=urllib.urlencode(caption_dict),
            method=urlfetch.POST)
        new_meme_dict = json.loads(result.content)
        picture_url = new_meme_dict['data']['url']
            # self.response.write(textz2);
            # picz = 'https://pbs.twimg.com/profile_images/764112991826698240/_4CpiqnH_400x400.jpg'
        # self.response.write("my post handler - your name was {meme_type}".format(meme_type=meme_type))
        template = template_env.get_template('templates/meme_results.html')
        # resultz = {'pic': picz}
        pic ={'pic':picture_url}

        # data = {'img_src': 'https://i.imgflip.com/1otk96.jpg'}
        self.response.write(template.render(pic))

    # def post(self):
    #     meme_types = self.request.get('meme-types')
    #     self.response.write("my post handler - your name was {meme_type}".format(meme_types=meme_types))
    #




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/meme', MemeType),
    ('/meme_temp', MemeType),
    ('/meme_result', MemeResults),
    ('/meme_results', MemeResults)



], debug=True)
