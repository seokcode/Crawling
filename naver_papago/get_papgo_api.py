import requests
from tqdm import tqdm
import pandas as pd

from config.environ import Environ



class NaverPapago:
    def get_data(self, word_list):
        word_ko_list = []
        word_en_list = []
        header = {"X-Naver-Client-Id": Environ.NAVER_CLIENT_ID, "X-Naver-Client-Secret": Environ.NAVER_CLIENT_SECRET}
        for word in tqdm(word_list):
            data = {'text': f"{word}",
                    'source': 'en',
                    'target': 'ko'}
            url = "https://openapi.naver.com/v1/papago/n2mt"
            response = requests.post(url, headers=header, data=data)
            send_data = response.json()
            try:
                trans_data = (send_data['message']['result']['translatedText'])
                word_ko_list.append(trans_data)
                word_en_list.append(word)
            except:
                word_ko_list.append("x")
                word_en_list.append(word)
                print("없음")

        df = pd.DataFrame({"name_en": word_en_list, "name_ko": word_ko_list})
        return df

if __name__ == '__main__':
    word_list = ["foggy"]
    a = NaverPapago().get_data(word_list)
    print(a)
