#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('blog.views'),
    url(r'^bloglist/$',        'blog_list',     name='blog_list'),
    url(r'^(?P<id>\d+)/$',     'blog_show',     name='blog_show'),
    url(r'^search/$',            'blog_search',     name='blog_search'),
    url(r'^tag/(?P<id>\d+)/$', 'blog_filter',   name='blog_filter'),
    url(r'^category/(?P<id>\d+)/$', 'blog_category',   name='blog_category'),
)