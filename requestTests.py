#helpful documentation:

#requests library:
#https://requests.readthedocs.io/en/latest/user/quickstart/

#beautiful soup:
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
import bs4

if __name__ == "__main__":
    url = input("enter url: ")
    r = requests.get(url)
    html = r.text#.text gets html of webpage
    exampleSoup = bs4.BeautifulSoup(html, 'html.parser')
    print("Soup:\n", exampleSoup)
    print("Find all urls within page: ")
    for link in exampleSoup.find_all('a'):
        print(link.get('href'))
    

