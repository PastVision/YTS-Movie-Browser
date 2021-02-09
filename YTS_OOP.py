import requests, tabulate
from func_timeout import func_set_timeout
from proxieshandler import ProxyHandler
import pyperclip as clip

class yts:
    DOMAINS = ['https://yts.mx', 'https://yts.pm', 'https://yts.vc', 'https://yts.unblockit.top', 'https://yts.unblockit.eu', 'https://yts.unblocked.lc', 'https://yts.ai']
    USE = 0
    __trackers = '&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969'
    requestURL = '/api/v2/list_movies.json'
    urlTorrent = '/torrent/download/'
    connected = False
    useProxy = False
    def __init__(self):
        try:
            if self.__pingTest() == 200:
                self.useProxy = False
                self.connected = True
        except:
            self.useProxy = True
            print('Your ISP has Blocked YTS!, Will use proxy!')
            self.__px = ProxyHandler(self.DOMAINS[self.USE]+self.requestURL)
            for proxy in self.__px.proxyList:
                try:
                    self.__pingTest(proxy)
                    self.proxyToUse = proxy
                    self.connected = True
                    break
                except:
                    continue
        if self.connected:
            self.urlYTS = self.DOMAINS[self.USE]+self.requestURL
            print(f'Connected to {self.DOMAINS[self.USE]}')
        else:
            print('Cannot connect to YTS, Check your Network')

    @func_set_timeout(5)
    def __pingURL(self, url, proxy=None):
        status = requests.get(url, proxies={'https':proxy}).status_code
        return status

    def __pingTest(self, proxy=None):
        for i, dom in enumerate(self.DOMAINS):
            print(f'DEBUG: Testing {dom}', end=' ')
            try:
                status = self.__pingURL(dom+self.requestURL, proxy)
            except:
                status = 404
            print(f'STATUS = {status}')
            if status == 200:
                self.USE = i
                break
        return status

    def __search(self, page = 1):
        try:
            if self.useProxy:
                return requests.get(f'{self.url}&page={page}',allow_redirects=True,proxies={'https':self.proxyToUse}).json()
            else:
                return requests.get(f'{self.url}&page={page}',allow_redirects=True).json()
        except Exception as e:
            print(f'An error Occourred: {e}')
            self.connected = False

    def search(self, keyword = '', limit = 20, minRating = 0, genre = '', quality = 'All', sortBy='year', orderBy='asc', page = 1):
        self.searchResult = list()
        self.moviesList = list()
        self.url = f'{self.urlYTS}?limit={limit}&minimum_rating={minRating}&query_term={keyword}&genre={genre}&quality={quality}&sort_by={sortBy}&order_by={orderBy}'
        if not self.connected:
            print('Not connected to YTS!')
            return

        self.searchResult.append(self.__search())

        self.countResult = self.searchResult[0]['data']['movie_count']
        if self.countResult == 0:
            print(f'No results for {keyword}.')
            return
        self.pages = self.countResult//limit + 1 if self.countResult//limit != self.countResult/limit else self.countResult//limit
        print(f'Found {self.countResult} results in {self.pages} page(s)!')
        for i in range(1,self.pages+1):
            self.moviesList.append(self.__search(i)['data']['movies'])

        #return

    def displayResults(self, page = 1):
        rows = list()
        j=0
        print(f'Page {page}: \n')
        for i in self.moviesList[page-1]:
            j+=1
            rows.append([j, i['title_english'], i['year'], len(i['torrents']), i['rating']])
        rows.append([])
        print(tabulate.tabulate(rows, ['No.', 'Title', 'Year', 'Qualities', 'IMDb Rating']))

    def displayQualities(self, page = 0, sel = 1):
        self.quals = self.moviesList[page][sel-1]['torrents']
        self.qualityCount = len(self.quals)
        rows = list()
        j=0
        for i in self.quals:
            j+=1
            rows.append([j, i['quality'], i['type'], i['size']])
        rows.append([])
        print(tabulate.tabulate(rows, ['No.', 'Qualities', 'Type', 'Size']))

    def makeMagnet(self, has, name):
        magnet = f'magnet:?xt=urn:btih:{has}&dn={name}-{self.__trackers}'
        return magnet

    def help(self):
        print('Usage:\n yts.search(keyword, limit, minRating, genre, quality, sortBy, orderBy)')
        print("\nDefaults:\n keyword = ''\tString\n limit = 20\tInteger between 1 - 50 (inclusive)\n minRating = 0\tInteger between 0 - 9 (inclusive)\n genre = 'All'\tString (For list of genres, use yts.listGenres())\n quality = 'All'\tString (720p, 1080p, 2160p, 3D)\n sortBy='year'\tString (title, year, rating, peers, seeds, download_count, like_count, date_added)\n orderBy='desc'\tString (desc, asc)\n")

    def listGenres(self):
        print('Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film Noir, History, Horror, Music, Musical, Mystery, Romance, Sci-Fi, Short Film, Sport, Superhero, Thriller, War, Western')
