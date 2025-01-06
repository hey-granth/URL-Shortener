from hashids import Hashids
from dotenv import load_dotenv
import os

# This is the service layer of the application. It is responsible for handling the business logic of the application.

load_dotenv()

# This is a dictionary that stores the original URL and the shortened URL. This is to ensure that the same URL is not shortened multiple times.
url_store = {}
hashids = Hashids(min_length=5, salt=os.environ.get("HASHID_SALT"))

def shorten_url(url):
    if url in url_store:
        return url_store[url]

    small_url = hashids.encode(len(url_store) + 1)
    url_store[small_url] = url
    return small_url

def get_original_url(small_url):
    return url_store.get(small_url)