# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    collections = 'users'

    user_id = Field()
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


class UserBaseItem(Item):
    collections = 'user_base'

    user_id = Field()
    name = Field()


class RemarkItem(Item):
    collections = 'remarks'


class BlogItem(Item):
    collections = 'blog'

    create_at = Field()
    blog_id = Field()
    text = Field()
    user_id=Field() # 由谁发表的
    user_name=Field()
    forward_count=Field()   # 转发数
    comments_count=Field()  # 评论数
    attitudes_count=Field() # 点赞数
