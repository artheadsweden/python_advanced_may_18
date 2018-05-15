from functools import wraps
import time
import requests

caching = True

def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = requests.get(url).text
    saved[url] = page
    return page

def cache(func):
    saved = {}
    @wraps(func)
    def cacher(arg):
        if arg in saved and caching:
            return saved[arg]
        result = func(arg)
        saved[arg] = result
        return result
    return cacher


@cache
def web_lookup2(url):
    return requests.get(url).text

def main():
    start_time = time.time()
    result = web_lookup2("http://cnn.com")
    end_time = time.time()
    print(end_time - start_time, "seconds")

    start_time = time.time()
    result = web_lookup2("http://cnn.com")
    end_time = time.time()
    print(end_time - start_time, "seconds")


if __name__ == '__main__':
    main()