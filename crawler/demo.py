from crawler.print_tree import *
from crawler.get_bs4 import *
import requests as httpreq
import json, shutil, threadpool


def crawle_douban(method):
    file_path = os.path.join(STATIC_ROOT, "data\\").replace('\\', '/')
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    if os.path.exists(file_path + '0'):
        shutil.rmtree(file_path + '0')
    if method == 'true':
        html = r'https://api.douban.com/v2/movie/top250?start={page}'
        i = 1
        p = 1
        while p <= 1:
            try:
                hjson = json.loads(httpreq.get(html.format(page=(p - 1) * 20)).text)
            except Exception as e:
                return
            # 处理json，具体返回样例参照豆瓣API即可，输出格式：  排行：电影中文名---英文名（年代）
            for key in hjson['subjects']:
                line = [str(i), key['title'], key['original_title'], key['year']]
                csv_line(line, 0, 0, '0', [])
                i += 1
            p += 1
    else:
        html = "https://api.douban.com/v2/book/search"
        book_tag_lists = ['计算机', '机器学习', 'linux', 'android', '数据库', '互联网']
        i = 1
        p = 0
        while p < len(book_tag_lists):
            dic = {'tag': book_tag_lists[p]}
            try:
                hjson = json.loads(httpreq.get(html, dic).text)
            except Exception as e:
                print(e)
            # 处理json，具体返回样例参照豆瓣API即可
            book_list = hjson['books']
            book_list = sorted(book_list, key=lambda x: float(x['rating']['average']), reverse=True)
            for key in book_list:
                line = [str(i), key['id'], key['title'], key['author'][0], key['rating']['average']]
                csv_line(line, 0, 1, '0', [])
                i += 1
            p += 1


def crawle_url(url, dep):
    bs4 = get_bs4(url)
    items = bs4.find_all("tr", {"class": "y2017"})
    contain = []
    for item in items:
        for child in item:
            get_string(child, contain)

    rank = 1
    le = len(contain)
    line = ['rank2017', 'rank2016', 'name', 'country',
            'value2017', 'value2017', 'value2016', 'value2016',
            'brand rating2017', 'brand rating2017', 'brand rating2016', 'brand rating2016']
    for i in range(0, le):
        if contain[i] == str(rank) and i + 1 < le and contain[i + 1] == str(rank):
            csv_line(line, 0, dep, '-1', [])
            line = []
            rank += 1
        else:
            line.append(contain[i])


def crawle_brand_finance():
    file_path = os.path.join(STATIC_ROOT, "data\\").replace('\\', '/')
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    if os.path.exists(file_path + '-1'):
        shutil.rmtree(file_path + '-1')
    urls = ["http://brandirectory.com/league_tables/table/global-500-2017",
            "http://brandirectory.com/league_tables/table/china-100-2017",
            "http://brandirectory.com/league_tables/table/us-500-2017"]
    deps = ["1", "2", "3"]
    func_var = []

    le = len(urls)

    for i in range(le):
        dic = {}
        dic['url'] = urls[i]
        dic['dep'] = deps[i]
        tmp = (None, dic)
        func_var.append(tmp)

    pool = threadpool.ThreadPool(len(urls))
    requests = threadpool.makeRequests(crawle_url, func_var)
    [pool.putRequest(req) for req in requests]
    pool.wait()
