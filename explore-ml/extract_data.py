import requests
from bs4 import BeautifulSoup

# url = "https://jamanetwork.com/journals/jamanetworkopen/article-abstract/2780267"
url = "https://clinicaltrials.gov/ct2/results?cond=alcohol"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'lxml')
print(soup.prettify())
table = soup.find('table', id='theDataTable')
print(table)
# h_tag = soup.find('h1', class_='meta-article-title')
# div_tag = soup.find('div', class_='heading-text thm-col sb-sc')

print(div_tag)
