#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import re

content =''' <head>
    </head>
    <h1>Signup</h1>
    <form action="/welcome" method="post">
    <label>Username:<label><input type="text" name="username"/><br>
    <label>Password:</label><input type="password" name="password"/><br>
    <label>Verify Password:</label><input type="password" name="verify"/><br>
    <label>Email(optional):</label><input type="text" name="email"/><br>
    <input type="submit"/>
    </form>'''

content_uer =''' <head>
    </head>
    <h1>Signup</h1>
    <form action="/welcome" method="post">
    <label>Username:<label><input type="text" name="username"/>Enter a valid username<br>
    <label>Password:</label><input type="password" name="password"/><br>
    <label>Verify Password:</label><input type="password" name="verify"/><br>
    <label>Email(optional):</label><input type="text" name="email"/><br>
    <input type="submit"/>
    </form>'''

content_pas =''' <head>
    </head>
    <h1>Signup</h1>
    <form action="/welcome" method="post">
    <label>Username:<label><input type="text" name="username"/><br>
    <label>Password:</label><input type="password" name="password"/>Enter a valid password<br>
    <label>Verify Password:</label><input type="password" name="verify"/><br>
    <label>Email(optional):</label><input type="text" name="email"/><br>
    <input type="submit"/>
    </form>'''

content_pasmatch =''' <head>
    </head>
    <h1>Signup</h1>
    <form action="/welcome" method="post">
    <label>Username:<label><input type="text" name="username"/><br>
    <label>Password:</label><input type="password" name="password"/><br>
    <label>Verify Password:</label><input type="password" name="verify"/>Password does not match<br>
    <label>Email(optional):</label><input type="text" name="email"/><br>
    <input type="submit"/>
    </form>'''

content_email =''' <head>
    </head>
    <h1>Signup</h1>
    <form action="/welcome" method="post">
    <label>Username:<label><input type="text" name="username"/><br>
    <label>Password:</label><input type="password" name="password"/><br>
    <label>Verify Password:</label><input type="password" name="verify"/><br>
    <label>Email(optional):</label><input type="text" name="email"/>Email not valid<br>
    <input type="submit"/>
    </form>'''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = """<head>
        </head>
        <h1>Signup</h1>
        <form action="/welcome" method="post">
        <label>Username:<label><input type="text" name="username"/><br>
        <label>Password:</label><input type="password" name="password"/><br>
        <label>Verify Password:</label><input type="password" name="verify"/><br>
        <label>Email(optional):</label><input type="text" name="email"/><br>
        <input type="submit"/>
        </form>"""
        self.response.write(content)

class Welcome(webapp2.RequestHandler):
    def post(self):
        greeting = "Thank you for signing up, "

        username = self.request.get("username")
        usre = re.compile("^[a-zA-Z0-9_-]{3,20}$")


        password = self.request.get("password")
        passre = re.compile("^.{3,20}$")

        email = self.request.get("email")
        emailre = re.compile("^[\S]+@[\S]+.[\S]+$")

        passverify = self.request.get("verify")

        if not usre.match(username):
            content = content_uer
        elif not passre.match(password):
            content = content_pas
        elif password != passverify:
            content = content_pasmatch
        elif not emailre.match(email):
            content = content_email
        else:
            content = "<h1>" + greeting + username + "!"+ "</h1>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
