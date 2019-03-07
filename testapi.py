from urllib import parse
import json
import requests

# url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&luicode=10000011&lfid=100103type=1&type=uid&value={uid}&containerid=100505{uid}'
# fans_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_6079534197&luicode=10000011&lfid=1005056079534197'
start_uid = (6079534197, 1676317545, 3237705130, 1851755225, 1823887605)

blog_url='https://m.weibo.cn/api/container/getIndex?uid=1676317545&luicode=10000011&lfid=100103type=1&type=uid&value=1676317545&containerid=1076031676317545'

# print(fans_url.replace('6079534197','{uid}'))
#
# #
# for uid in start_uid:
#     print(fans_url.format(uid=uid))
# fans_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&luicode=10000011&lfid=100505{uid}&since_id={page}'
# for uid in start_uid:
#     for page in range(1,3):
#         print(fans_url.format(uid=uid,page=page))
#
# print(fans_url.format(uid=start_uid[-1],page=2))
# response = requests.get(fans_url.format(uid=start_uid[-1],page=2))
# text = json.loads(response.text)
# print(text['data']['cards'][-1]['card_group'][2]['user']['id'])
# print(len(text['data']['cards'][-1]['card_group']))
# with open('user.json', 'w') as f:
#     f.write(json.dumps(text).encode('utf-8').decode('unicode_escape'))
