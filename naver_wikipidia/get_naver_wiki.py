import ssl
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
from tqdm import tqdm
from config.environ import Environ


class NaverWiki:

    def get_data(self, word_list):
        title_list = []
        description_list = []
        for word in tqdm(word_list):
            encText = urllib.parse.quote(word)
            ssl._create_default_https_context = ssl._create_unverified_context
            url = "https://openapi.naver.com/v1/search/encyc.xml?query={}".format(encText)
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", Environ.NAVER_CLIENT_ID)
            request.add_header("X-Naver-Client-Secret", Environ.NAVER_CLIENT_SECRET)
            response = urllib.request.urlopen(request)
            soup = bs(response, "html.parser")
            item = soup.find_all("item")
            try:
                title_list.append(item[0].find("title").text.replace('<b>','').replace('</b>',''))
                description_list.append(item[0].find("description").text.replace('<b>','').replace('</b>',''))
            except:
                title_list.append("x")
                description_list.append("x")
                print("없음")

        dic = {"word":word_list,"definition":description_list}
        df = pd.DataFrame.from_dict(dic, orient='index')
        df = df.transpose()
        return df

if __name__ == '__main__':
    word_list = ["개구리"]
    a = NaverWiki().get_data(word_list)
    print(a)

