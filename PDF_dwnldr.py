# libs
import requests
import csv

# .csv file with given URL's
# .csv file == ['index','title of book', 'URL']
url_file = r'C:\Users\hugoo\Node.js\csv_url.csv'

# DOWNLOADER
with open(url_file, 'r') as csv_file:
    # open file with mode read
    csv_reader = csv.reader(csv_file)
    # loop the file
    for line in csv_reader:
        # try:except in case of broken links dont stopping the scrip
        try:
            # get content info from URL
            pdf = requests.get(line[2]).content
            # create and save .pdf file
            open(line[0]+'-'+line[1]+'.pdf', 'wb').write(pdf)
        except Exception as e:
            print('Error')
    # When finished
    print('Done')
