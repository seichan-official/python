import requests
import bs4

class scraping():
    def rakuten_syoken(self,search_keyword):
    # URL指定
        search_URL = 'wss://exchange.rakuten-wallet.co.jp/ws' + search_keyword
        search_response = requests.get(search_URL)
    # 結果
        soup = bs4.BeautifulSoup(search_response.text,'lemx')
        parsed_page = soup.select('div.kCrYT>a')
        
        