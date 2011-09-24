#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from distutils import core
core.setup(
    name = "tmdb",
    packages = ["."],
    version = "1.0.0",
    description = "themoviedb.org python wrapper",
    author = "Doğan Aydın",
    author_email = "dogan1aydin@gmail.com",
    url = "https://github.com/doganaydin/themoviedb",
    download_url = "https://github.com/doganaydin/themoviedb/tarball/master",
)