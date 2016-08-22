#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instagram.client import InstagramAPI
import pandas as pd

access_token = "YOUR_ACCESS_TOKEN"
client_secret = "YOUR_CLIENT_SECRET"

api = InstagramAPI(access_token=access_token,
	               client_secret=client_secret)

recent_media, next_ = api.user_recent_media(user_id="archianya", count=1000)

for media in recent_media:
   print media.caption.text