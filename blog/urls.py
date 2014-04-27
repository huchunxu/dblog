#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('blog.views'),
    url(r'^$',                 'blog_list',     name='blog_list'),
    url(r'^(?P<id>\d+)/$',     'blog_detail',   name='blog_detail'),
    url(r'^search',            'blog_list',     name='blog_search'),
    url(r'^add',               'blog_list',     name='blog_add'),
    url(r'^tag/(?P<id>\d+)/$', 'blog_filter',   name='blog_filter'),
    url(r'^(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='comment_show'),
)