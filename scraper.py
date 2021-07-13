import requests
from bs4 import BeautifulSoup as bs 
import csv
from datetime import datetime
  
  

URL = [ 'https://www.amazon.in/Dell-15-6-inch-i7-10750H-NVIDIA1650-D560260WIN9BE/dp/B08H9PTSYR/ref=sr_1_2?dchild=1&qid=1625733394&refinements=p_89%3ADell%2Cp_n_feature_thirteen_browse-bin%3A12598163031&s=computers&sr=1-2',
        'https://www.amazon.in/dp/B08ZN6KNP1/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B08ZN6KNP1&pd_rd_w=o9zO7&pf_rd_p=f7411aaf-b7ff-4de1-8a53-cdd447bca5de&pd_rd_wg=a39qY&pf_rd_r=AXEZEDMACT2B2XRA10CE&pd_rd_r=578e4ede-16ac-4d3f-87a9-e1cadba86b22&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMTdTWjJONlBYNTk1JmVuY3J5cHRlZElkPUEwMzE2NzMyMk1aNDJLV0w1STZHVCZlbmNyeXB0ZWRBZElkPUEwNDg1MTc1Wk5ENTE5SjFCNDk0JndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==']

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for i in range(len(URL)):
    page = requests.get(URL[i], headers=headers)

    soup = bs(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

##(\-?\d+\.?\d{0,2})

    print(title.strip())
    print(price)



    with open('prices.csv', mode='w', encoding='utf-8') as price_file:
        price_writer = csv.writer(price_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        price_writer.writerow([title.strip(), price, datetime.today()])


