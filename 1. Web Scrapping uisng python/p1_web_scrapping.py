# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# empty list to store data
PhoneName = []
PhoneRating = []
PhoneSpecs = []
Price = []

# url form which we are extracting data
url = "https://www.flipkart.com/search?q=mobile%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
request = requests.get(url).content
soup = BeautifulSoup(request, "html.parser")
data = soup.findAll('a', href=True, attrs={'class': '_1fQZEK'})

for i in data:
    pName = i.find('div', attrs={'class': '_4rR01T'})
    pRating = i.find('div', attrs={'class': '_3LWZlK'})
    pSpecs = i.find('div', attrs={'class': 'fMghEO'})
    pPrice = i.find('div', attrs={'class': '_30jeq3 _1_WHN1'})

    PhoneName.append(pName.text)
    PhoneRating.append(pRating.text)
    PhoneSpecs.append(pSpecs.text)
    Price.append(pPrice.text)

# storing data in csv file
df = pd.DataFrame({'Phone Name': PhoneName, 'Rating': PhoneRating, 'Specs': PhoneSpecs, 'Price': Price})
df.to_csv('DS-PR1-18IT005.csv', index=False, encoding='utf-8')
