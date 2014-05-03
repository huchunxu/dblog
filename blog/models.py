# -*- coding: utf-8 -*-

from django.db import models


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, verbose_name=u'标签名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.tag_name


class Category(models.Model):
    """docstring for Category"""
    category_name = models.CharField(max_length=20, verbose_name=u'类名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.category_name


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30, verbose_name=u'作者名')
    email = models.EmailField(blank=True, verbose_name=u'邮箱')
    website = models.URLField(blank=True, verbose_name=u'个人网站')

    def __unicode__(self):
        return u'%s' % (self.name)


class Article(models.Model):
    """docstring for Article"""
    caption = models.CharField(max_length=30, verbose_name=u'标题')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发表时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    author = models.ForeignKey(Author, verbose_name=u'作者')
    category = models.ForeignKey(Category, blank=True, verbose_name=u'分类')
    content = models.TextField(verbose_name=u'内容')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')


