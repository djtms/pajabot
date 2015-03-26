Pajabot
=======

IRC bot &amp; utilities for hackerspace management. Target hw: Raspberry pi.

Dependencies:
* Python irclib, https://bitbucket.org/jaraco/irc
* Python Imaging Library fork (Pillow)
* Python Feedparser

Installing dependencies to Raspbian:

* pip install irc gevent feedparser Pillow zerorpc pyzmq

Running
=======

cp bot.conf local.conf
./bot/pajabot.py

