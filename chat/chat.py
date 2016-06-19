#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
Simplified chat demo for websockets. Slightly modified.
Original program can be found here:
https://github.com/tornadoweb/tornado/tree/master/demos/websocket

"""

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid

from tornado.options import define, options
from cleverbot import Cleverbot

cb = Cleverbot()
define("port", default=8888, help="run on the given port", type=int)

# Application: main manager of website
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [  # handler are the workers of the website
            (r"/", MainHandler),
            (r"/chatsocket", ChatSocketHandler),
            (r"/png", tornado.web.StaticFileHandler, {'path':'./'}),
        ]
        settings = dict(  # settings of tornado
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        super(Application, self).__init__(handlers, **settings)


class Handler(tornado.web.RequestHandler):
    """
    Handler for images
    """
    def get(self):
        self.render("html_image_05.html")


class MainHandler(tornado.web.RequestHandler):
    """
    Handler of the main page
    """
    def get(self):
        self.render("index.html", messages=ChatSocketHandler.cache)


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    """
    Handler of the chat
    """
    waiters = set()
    cache = []
    cache_size = 200

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        """
        Adds a user to the conversation

        :return:
        """
        ChatSocketHandler.waiters.add(self)

    def on_close(self):
        """
        Closes connection when user leavers

        :return:
        """
        ChatSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):
        """
        Write onto the chat

        :param chat:
        :return:
        """
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        """
        Sends response to the users
        :param chat:
        :return:
        """
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        """
        Writes message to message.html so it can be displayed

        :param message:
        :return:
        """
        logging.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            }
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat))

        ChatSocketHandler.update_cache(chat)
        ChatSocketHandler.send_updates(chat)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
