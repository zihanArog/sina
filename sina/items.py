# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    collections = 'users'

    id = Field()
    name = Field()
    blog_count = Field()
    verified = Field()
    verified_type = Field()
    verified_reason = Field()
    description = Field()
    fans_count = Field()
    gender = Field()
    follow_count = Field()
    avatar = Field()


class RemarkItem(Item):
    collections = 'remarks'


class BlogItem(Item):
    collections = 'blog'
