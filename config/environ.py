import os
from dotenv import load_dotenv

load_dotenv()


class Environ:
    R3_DB_HOST = os.environ['R3_DB_HOST']
    R3_DB_USER = os.environ['R3_DB_USER']
    R3_DB_PASS = os.environ['R3_DB_PASS']
    R3_DB_NAME = os.environ['R3_DB_NAME']

    # reference
    USER_AGENT = os.environ['USER_AGENT']
    KOREA_DICT_API_KEY = os.environ['KOREA_DICT_API_KEY']
    NAVER_CLIENT_ID = os.environ['NAVER_CLIENT_ID']
    NAVER_CLIENT_SECRET = os.environ['NAVER_CLIENT_SECRET']
