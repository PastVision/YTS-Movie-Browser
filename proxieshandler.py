import requests
from lxml.html import fromstring
from func_timeout import func_set_timeout
class ProxyHandler:
    url = 'https://free-proxy-list.net/'
    proxyList = list()

    def __init__(self, testURL):
        self.testURL = testURL
        print('Testing cached Proxies, Might take a while...')
        try:
            for proxy in self.__load():
                try:
                    self.__testProxy(proxy)
                except:
                    continue
            self.__save(self.proxyList)
            if len(self.proxyList) == 0:
                print('Getting New Proxies...')
                self.__getProxy()
                self.__save(self.proxyList)
            print('Proxies loaded successfuly!')
        except:
            print('An ERROR Occourred! Check Network!')

    def __getProxy(self):
        response = requests.get(self.url)
        parser = fromstring(response.text)
        for i in parser.xpath('//tbody/tr')[:20]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                try:
                    self.__testProxy(proxy) 
                except:
                    continue

    @func_set_timeout(5)
    def __testProxy(self,proxy):
        if requests.get(self.testURL,allow_redirects=True,proxies={'https':proxy}).status_code == 200:
            if proxy not in self.proxyList:
                self.proxyList.append(proxy)

    def __save(self,dat):
        with open('proxies', 'w') as f:
            for data in dat:
                f.writelines("%s\n" % data)
            f.close()

    def __load(self):
        data = list()
        try:
            with open('proxies', 'r') as f:
                content = f.readlines()
                for line in content:
                    current_place = line[:-1]
                    data.append(current_place)
        except:
            with open('proxies', 'w') as f: f.close()
        return data

if __name__ == '__main__':
    px = ProxyHandler('http://')
