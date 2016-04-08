import urllib.request
from io import BytesIO
import gzip
import json
import os.path
import logging


class HttpRequest:
    def __init__(self):
        pass
    def __build_header(self):
        header = dict()
        header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        header['Accept-Encoding'] = 'gzip,deflate,sdch'
        header['Accept-Language'] = 'en-US,en;q=0.8'
        header['Connection'] = 'keep-alive'
        header['DNT'] = '1'
        header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36'
   
        return header

    def get(self, url):
        """
        A GET request to the url and returns the content of that url in str type
        """

        logging.info("http_request", "GET {0}".format(url))

        request = urllib.request.Request(url = url, headers = self.__build_header())
        fp = urllib.request.urlopen(request)
        http_message = fp.info()
        content = fp.read()
        fp.close()
        
        content_len = len(content)
        logging.info("http_request", "GET {0} ... OK {1} Bytes".format(url, content_len))

        if http_message.get('Content-Encoding') == 'gzip':
            buf = BytesIO(content)
            f = gzip.GzipFile(fileobj = buf)
            content = f.read()
            logging.info("http_request", "unzip {0} -> {1}".format(content_len, len(content)))
        
        return content.decode('utf-8')

    def post(self, url, data):
        """
        A POST request to the url and returns the content in str type

        Not implemented
        """

        return ""

if __name__=='__main__':
    hr = HttpRequest()
    url = 'http://www.xiachufang.com/recipe/92086/'
    string = hr.get(url)
    # print(string)