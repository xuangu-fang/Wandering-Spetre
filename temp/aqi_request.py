import requests

"""search API #
request"""

headers = {}

json_data = {
    'keyword': '三体',
    'page': 1,
    'sensitive': False,
}

response = requests.post('https://api.ylibrary.org/api/search/', headers=headers, json=json_data)
'''
return

{
  "data": [
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": "9787536692930",
      "extension": "pdf",
      "filesize": 4706425,
      "year": "",
      "id": 2817721,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": null,
      "extension": "txt",
      "filesize": 399897,
      "year": "",
      "id": 3483639,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "重庆出版社",
      "isbn": "9787536692930",
      "extension": "pdf",
      "filesize": 165383382,
      "year": "2008",
      "id": 5241719,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": null,
      "extension": "epub",
      "filesize": 2134513,
      "year": "2011",
      "id": 5552637,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": null,
      "extension": "azw3",
      "filesize": 386569,
      "year": "2011",
      "id": 5732339,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "重庆出版社",
      "isbn": null,
      "extension": "pdf",
      "filesize": 13713550,
      "year": "2012",
      "id": 5814476,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "epub掌上书苑",
      "isbn": null,
      "extension": "epub",
      "filesize": 2135075,
      "year": "2011",
      "id": 6165958,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "epub掌上书苑",
      "isbn": null,
      "extension": "mobi",
      "filesize": 4632483,
      "year": "2011",
      "id": 6196050,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "epub掌上书苑",
      "isbn": null,
      "extension": "mobi",
      "filesize": 3336354,
      "year": "2011",
      "id": 11552744,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣 & chenjin5.com",
      "publisher": "chenjin5.com 海量电子书免费下载",
      "isbn": null,
      "extension": "azw3",
      "filesize": 611342,
      "year": "2011",
      "id": 11896657,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣 & chenjin5.com [刘慈欣 & chenjin5.com]",
      "publisher": "chenjin5.com 海量电子书免费下载",
      "isbn": null,
      "extension": "epub",
      "filesize": 331077,
      "year": "2011",
      "id": 11903485,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣 & chenjin5.com",
      "publisher": "chenjin5.com 海量电子书免费下载",
      "isbn": null,
      "extension": "mobi",
      "filesize": 589795,
      "year": "2011",
      "id": 11913070,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "epub掌上书苑",
      "isbn": null,
      "extension": "mobi",
      "filesize": 3333653,
      "year": "2011",
      "id": 11993964,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "epub掌上书苑",
      "isbn": null,
      "extension": "azw3",
      "filesize": 3417755,
      "year": "2011",
      "id": 15425721,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": "9787229042066",
      "extension": "azw3",
      "filesize": 386573,
      "year": "2011",
      "id": 15959349,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "劉慈欣",
      "publisher": "早川書房",
      "isbn": null,
      "extension": "txt",
      "filesize": 989016,
      "year": "",
      "id": 16310451,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": "9787229042066",
      "extension": "mobi",
      "filesize": 602933,
      "year": "2011",
      "id": 16337681,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "",
      "isbn": "9787229042066",
      "extension": "mobi",
      "filesize": 602601,
      "year": "2011",
      "id": 16530802,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "原著：刘慈欣",
      "publisher": "",
      "isbn": null,
      "extension": "pdf",
      "filesize": 1242036,
      "year": "",
      "id": 16566326,
      "source": "zlibrary"
    },
    {
      "title": "三体",
      "author": "刘慈欣",
      "publisher": "epub掌上书苑",
      "isbn": null,
      "extension": "epub",
      "filesize": 2135060,
      "year": "2011",
      "id": 16566339,
      "source": "zlibrary"
    }
  ],
  "hits": 900
}'''

import requests

headers = {}

json_data = {
    'id': 2817721,
    'source': 'zlibrary',
}

response = requests.post('https://api.ylibrary.org/api/detail/', headers=headers, json=json_data)

"""
return
{
  "title": "三体",
  "author": "刘慈欣",
  "isbn": "9787536692930",
  "extension": "pdf",
  "filesize": 4706425,
  "pages": "315",
  "md5": "697ea3f464ba71eeca0ce9e34d2606da",
  "ipfs_cid": "bafykbzaceaqrdm4hc3qwqawhgdb2fwvewvjiyp7yyfzcohypbbg6ibdeuyfvg",
  "id": 2817721,
  "source": "z-library"
}"""