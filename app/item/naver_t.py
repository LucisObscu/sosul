import urllib.request as ur
import urllib.parse as ps
import ast



def naver_translate(srch,before,after):
    k = {'한국어': 'ko',
         '영어': 'en',
         '중국어 간체': 'zh-CN',
         '중국어 번체': 'zh-TW',
         '스페인어': 'es',
         '프랑스어': 'fr',
         '베트남어': 'vi',
         '태국어': 'th',
         '인도네시아어': 'id',
         '일본어':'ja'}
    client_id = "eBVkHawd8iCnqtm5cSRa"
    client_secret = "giD28l9evC"
    encText = ps.quote(srch)
    data = "source={0}&target={1}&text=".format(k[before],k[after]) + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request_url = ur.Request(url)
    request_url.add_header("X-Naver-Client-Id", client_id)
    request_url.add_header("X-Naver-Client-Secret", client_secret)
    response_naver = ur.urlopen(request_url, data=data.encode("utf-8"))
    return ast.literal_eval(response_naver.read().decode('utf-8'))['message']['result']['translatedText']