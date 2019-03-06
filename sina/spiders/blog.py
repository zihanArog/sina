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
    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&luicode=10000011&lfid=100505{uid}'

    def start_requests(self):
        for uid in self.start_uid:
            yield scrapy.Request(url=self.user_url.format(uid=uid), callback=self.parse_user)

    def parse_user(self, response):
        text = json.loads(response.text)
        user_item = UserItem()
        field_map = {
            'id': 'id',
            'name': 'screen_name',
            'blog_count': 'statuses_count',
            'verified': 'verified',
            'verified_type': 'verified_type',
            'verified_reason': 'verified_reason',
            'description': 'description',
            'fans_count': 'followers_count',
            'gender': 'gender',
            'follow_count': 'follow_count',
            'avatar': 'avatar_hd'
        }

        for (field, attr) in field_map.items():
            user_item[field] = text['data']['userInfo'][attr]
        return user_item
        # 爬粉丝信息
        yield scrapy.Request(url=self.fans_url.format(uid=uid),callback=self.parse_fans)

    def parse_fans(self, response):

        pass
