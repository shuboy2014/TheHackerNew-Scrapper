from  bs4 import BeautifulSoup
import urllib

url = 'http://thehackernews.com/'

response = urllib.urlopen(url)

html = response.read()

soup = BeautifulSoup(html,'lxml')  

new_number=1
for tag in soup.find_all('a') :
    if tag.get('class')!= None and  tag['class'] == ['url','entry-title']:
        print new_number , tag.get_text()
        new_number+=1