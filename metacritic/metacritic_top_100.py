from datetime import datetime

import pandas as pd
from tqdm import tqdm
from connect.web_factory import WebFactory

now = datetime.now()


class MetaCriticTop100:

    def get_html(self):
        url = "https://www.metacritic.com/browse/games/score/metascore/90day/all/filtered"
        soup = WebFactory().get_request(url, '')
        data = soup.select('td.clamp-summary-wrap')
        return data

    def get_game_name(self):
        name = []
        for date_list in tqdm(self.get_html()):
            data1 = date_list.select_one('h3')
            name.append(data1.text)
        return name

    def create_dataframe(self):
        name = self.get_game_name()
        df = pd.DataFrame({'name': name})
        df.to_csv(f"Metacritic_top100_{now.year}-{now.month}-{now.day}.csv")
        return df


if __name__ == '__main__':
    a = MetaCriticTop100().create_dataframe()
    print(a)
