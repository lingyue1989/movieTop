"""
爬取最新电影榜单
url：http://dianying.2345.com/top/
使用requests--》bs4路线
Python版本：3.6
OS 版本 Mac OS 10.14.3
Date: 2019-3-13
作者：Wardwill
"""



import requests
import bs4
import lxml



# 获得html内容
def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        # 请求是否成功
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text

    except:
        print('error')


# 获取内容
def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html,'lxml')

    # 找的电影li
    movie_list = soup.find('ul',class_='picList clearfix')
    movies = movie_list.find_all('li')

    for top in movies:
        # finf pic url
        pic_url = 'http:' + top.find('img')['src']

        name = top.find('span', class_='sTit').a.text

        try:
            time = top.find('span', class_='sIntro').text
        except:
            time = '无上映时间'

        actors = top.find('p', class_='pActor')
        actor = ''
        if actors is None:
            actor = 'ooooo'

        else:
            for act in actors.contents:
                actor += act.string + '  '

        movie_info = top.find('p', class_= 'pTxt pIntroShow').text

        print('片名：{} \t {} \n {} \n {} \n \n'.format(name, time, actor, movie_info))

        with open('/Users/wuwei/Documents/98-Python/pycharmSpace/test003/' +name+'.png', 'wb+') as f:
            f.write(requests.get(pic_url).content)

def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == '__main__':
    main()






