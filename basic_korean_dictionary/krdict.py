import pandas as pd
from tqdm import tqdm
from config.environ import Environ
from connect.web_factory import WebFactory


class BasicKoreaDictionary:

    def get_data(self, search_name):
        definition_list = []
        word_list = []
        name_list = [search_name]
        for name in tqdm(name_list):
            url = f"https://krdict.korean.go.kr/api/search?key={Environ.KOREA_DICT_API_KEY}&q={name}"
            soup = WebFactory().get_request(url, "verify")
            try:
                item = soup.find_all("item")
                word_list.append(item[0].find("word").text)
                definition_list.append(item[0].find("definition").text)
            except:
                word_list.append("x")
                definition_list.append("x")

        df = pd.DataFrame({"word": word_list,
                           "definition": definition_list})
        return df


if __name__ == '__main__':
    a = BasicKoreaDictionary().get_data("개구리")
    print(a)
