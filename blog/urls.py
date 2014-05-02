#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('blog.views'),
    url(r'^bloglist/$',        'blog_list',     name='blog_list'),
    url(r'^(?P<id>\d+)/$',     'blog_show',     name='blog_show'),
    url(r'^search/$',            'blog_search',     name='blog_search'),
    url(r'^add/$',               'blog_add',     name='blog_add'),
    url(r'^(?P<id>\w+)/update/$', 'blog_update', name='blog_update'),
    url(r'^(?P<id>\w+)/del/$', 'blog_del',      name='blog_del'),
    url(r'^tag/(?P<id>\d+)/$', 'blog_filter',   name='blog_filter'),
    url(r'^category/(?P<id>\d+)/$', 'blog_category',   name='blog_category'),
    url(r'^(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='comment_show'),
)