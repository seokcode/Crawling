from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import datetime
from tqdm import tqdm

from connect.web_factory import WebFactory

now = datetime.datetime.now()


class IgdbTop100:
    def get_html(self):
        url = "https://www.igdb.com/top-100/games"
        driver = WebFactory().get_driver('headless')
        driver.get(url)
        html = driver.page_source
        driver.close()
        return html

    def get_game_name(self):
        name = []
        soup = bs(self.get_html(), "html.parser")
        time.sleep(1)
        data = soup.select('td > a')
        for data1 in tqdm(data):
            name.append(data1.text)
        return name

    def create_dataframe(self):
        name = filter(None, self.get_game_name())
        df = pd.DataFrame(dict(name=name))
        df.to_csv(f"Igdb_top100_{now.year}-{now.month}-{now.day}.csv")
        return df


if __name__ == '__main__':
    a = IgdbTop100().create_dataframe()
    print(a)