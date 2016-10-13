#!/usr/bin/env python

__all__ = ['toutiao_download']

from ..common import *
import json
import time

def toutiao_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    download_urls([url], "notitle.mp4", 'mp4', None, output_dir, merge = merge)

site_info = "toutiao.com"
download = toutiao_download
download_playlist = playlist_not_supported('toutiao')
