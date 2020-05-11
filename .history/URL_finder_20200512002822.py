# libs
from bs4 import BeautifulSoup
import requests
import csv

# open file to write fixed URL's
csv_url = open('csv_url.csv', 'w')
# since its a .csv file we need to use csv lib to write to it
csv_writer = csv.writer(csv_url)

with open(r'books.csv') as csv_file:
    # get url from .csv
    books = csv.reader(csv_file)
    # skip first line
    next(books)
    # loop all lines
    for line in books:
        # get infro from url
        r = requests.get(line[2]).text
        # get HTML info
        soup = BeautifulSoup(r, 'lxml')
        # try:except: in case of broken link (or paid book)
        try:
            # find keyword article in HTML fetched
            article = soup.find('article')
            # the correct part of the link is inside this class, we need to find it like so
            url_certo = article.find(
                'div', class_='cta-button-container__item').div.a['href']
            # adding first part of the link
            url_certissimo = 'https://link.springer.com/' + url_certo
            # write link and index into the new .csv file
            csv_writer.writerow([line[0], line[1], url_certissimo])
        except Exception as e:
            print('Error')
# close file
csv_url.close()
