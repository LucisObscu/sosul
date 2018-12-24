from django.shortcuts import render
from time import sleep
import urllib.request as req
from bs4 import BeautifulSoup
from django.utils import timezone

from app.item.naver_t import naver_translate
from app.models import Sosul


def urlerror(url):
    try:
        return req.urlopen(url)
    except:
        sleep(2)
        return urlerror(url)


def view_sing(request):
    key='qjtmxjtlfqj!2'
    if request.session.get('pw', False)  == key:
        if request.method == 'POST':
            word = request.POST['word']
            try:
                data=Sosul.objects.get(keyword=word)
                with open(data.data_path,'rt',encoding='utf-8') as f:
                    word_data_test = f.read().split('/n')
                return render(
                    request,
                    'insert_views.html',
                    {
                        'word_data_list': word_data_test,
                        'ok':1
                    }
                )

            except:
                org_url = 'https://ncode.syosetu.com/{0}/'.format(word)
                urls = urlerror(org_url)
                soup = BeautifulSoup(urls, 'html.parser')
                title = soup.select('.novel_title')[0].get_text()
                count = len(soup.select('.novel_sublist2'))
                word_data = ''
                word_data_test = []
                for i in range(count):
                    urlo = urlerror(org_url + str(i + 1) + '/')
                    soups = BeautifulSoup(urlo, 'html.parser')
                    for i in soups.select('.novel_view p'):
                        word_data += i.get_text() + '/n'
                        word_data_test.append(i.get_text())
                ko_title = naver_translate(title, '일본어', '한국어')
                path = 'app/data/{0}.txt'.format(ko_title)
                with open(path, 'wt', encoding='utf-8') as f:
                    f.write(word_data)
                Sosul.objects.create(title=title, ko_title=ko_title, update_count=count, data_path=path, link=org_url,
                                     keyword=word, date=timezone.now())
                return render(
                    request,
                    'insert_views.html',
                    {
                        'word_data_list': word_data_test,
                        'ok': 1
                    }
                )
        else :
            return render(
                request,
                'insert_views.html',
                {
                    'data_views_list':Sosul.objects.all(),
                    'ok':1
                }
            )
    return render(
        request,
        'login.html'
    )

def get_view(request,word):
    key = 'qjtmxjtlfqj!2'
    if request.session.get('pw', False) == key:
        data_word=Sosul.objects.get(keyword=word)
        with open(data_word.data_path,'rt',encoding='utf-8') as f:
            word_data_test = f.read().split('/n')
        return render(
            request,
            'insert_views.html',
            {
                'word_data_list': word_data_test,
                'ok':1
            }
        )
    return render(
        request,
        'login.html'
    )

def login(request):
    key = 'qjtmxjtlfqj!2'
    if request.method == 'POST':
        if request.POST['pw'] == key or request.session.get('pw', False) == key:
            request.session['pw']=key
            return render(
                request,
                'login.html',
                {
                    'ok':1
                }
            )
        else:
            return render(
                request,
                'login.html'
            )
    else:
        return render(
            request,
            'login.html'
        )


def sb(request,pw,keyword):
    if pw == 'qjtmxjtlfqj!2':
        data_word = Sosul.objects.get(keyword=keyword)
        with open(data_word.data_path, 'rt', encoding='utf-8') as f:
            word_data_test = f.read().split('/n')
        return render(
            request,
            'insert_views.html',
            {
                'word_data_list': word_data_test,
                'ok': 1
            }
        )
    else:
        return render(
            request,
            'login.html'
        )