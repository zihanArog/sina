# -*- coding: utf-8 -*-
import scrapy
import json
from sina.items import *

class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['m.weibo.cn']
    # 起始url，用start_request代替
    # start_urls = ['http://m.weibo.cn/']

    start_uid = (6079534197, 1676317545, 3237705130, 1851755225, 1823887605)

    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&luicode=10000011&lfid=100103type=1&type=uid&value={uid}&containerid=100505{uid}'
    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&luicode=10000011&lfid=100505{uid}&since_id={page}'
    blog_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&luicode=10000011&lfid=100103type=1&type=uid&value={uid}&containerid=107603{uid}&page={page}'

    def start_requests(self):
        for uid in self.start_uid:
            yield scrapy.Request(url=self.user_url.format(uid=uid), callback=self.parse_user, meta={'uid': uid})

    def parse_user(self, response):
        text = json.loads(response.text)
        user_item = UserItem()
        field_map = {
            'user_id': 'id',
            'name': 'screen_name',
            'blog_count': 'statuses_count',
            'verified': 'verified',
            'verified_type': 'verified_type',
            # 'verified_reason': 'verified_reason',
            'description': 'description',
            'fans_count': 'followers_count',
            'gender': 'gender',
            'follow_count': 'follow_count',
            'avatar': 'avatar_hd'
        }

        for (field, attr) in field_map.items():
            user_item[field] = text['data']['userInfo'][attr]
        yield user_item
        uid = response.meta['uid']
        # 爬粉丝信息
        yield scrapy.Request(url=self.fans_url.format(uid=uid, page=1), callback=self.parse_fans,
                             meta={'uid': uid, 'page': 1})
        # 爬取微博信息
        yield scrapy.Request(url=self.blog_url.format(uid='uid', page=1), callback=self.parse_blog,
                             meta={'uid': uid, 'page': 1})

    def parse_fans(self, response):
        """

        :param response:
        :return:
        """
        uid = response.meta['uid']
        page = response.meta['page'] + 1
        text = json.loads(response.text)
        # 这个是一个页面里面人数
        user_count = len(text['data']['cards'][-1]['card_group'])
        user_base_item = UserBaseItem()
        for i in range(user_count):
            uid = text['data']['cards'][-1]['card_group'][i]['user']['id']
            user_base_item['user_id'] = uid
            user_base_item['name'] = text['data']['cards'][-1]['card_group'][i]['user']['screen_name']

            # 返回item
            yield user_base_item
            # 爬取该用户的信息
            yield scrapy.Request(url=self.user_url.format(uid=uid), callback=self.parse_user, meta={'uid': uid})

        # 爬取下一页的fans
        yield scrapy.Request(url=self.fans_url.format(uid=uid, page=page), callback=self.parse_fans,
                             meta={'uid': uid, 'page': page})

    def parse_blog(self, response):
        '''
        爬取一页信息
        :param response:
        :return:
        '''
        uid = response.meta['uid']
        page = response.meta['page'] + 1
        text = json.loads(response.text)
        field_map = {
            'create_at': 'create_at',
            'blog_id': 'id',
            'text': 'text',
            'forward': 'reposts_count',
            'comments_count': 'comments_count',
            'attitudes_count': 'attitudes_count'
        }

        for i in range(len(text['data']['cards'])):

            # 存入blog信息
            blog_item = BlogItem()
            for (attr, field) in field_map.items():
                blog_item['attr'] = text['data']['cards'][i]['mblog'][field]
            blog_item['user_id'] = text['data']['cards'][i]['mblog']['user']['id']
            blog_item['user_name'] = text['data']['cards'][i]['mblog']['user']['screen_name']

            yield blog_item
        # 下一页微博
        yield scrapy.Request(url=self.blog_url.format(uid=uid, page=page), callback=self.parse_blog,
                             meta={'uid': uid, 'page': page})
