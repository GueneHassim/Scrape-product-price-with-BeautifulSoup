import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

MY_SENDING_NUMBER = "+13016913859"
MY_RECEIVING_NUMBER = "RECEIVER NUMBER"
TWILLIO_SID = "AC14b819a94a7af51864305057264e999d"
TWILLIO_AUTHTOKEN = "c148682c7e885e3c14de63508bb72cc8"

# Setting target price(1.0 = 1k)
TARGET_PRICE = 2.500  # €
# URL and requests headers parameters.
URL = "https://eu.formovie.com/products/formovie-theater-4k-laser-projector"
parameters = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.7"}

# Get in touch with the URL page.
response = requests.get(url=URL, headers=parameters).text
# print(response)
soup = BeautifulSoup(response, "html.parser")

# Searching for the product page title and saving it into a variable.
product_title = soup.find(name="h1", class_="h2 mb-4 product-title").text
# print(product_title)

# Searching for the product price and saving it into a variable.
product_price_data = (soup.find(name="span", class_="h2 fs-2 price-item price-item--sale as-price-sale").text)
cleaning_price_data = (product_price_data.split("\n")[1]).split(" ")[10]
product_price = float((cleaning_price_data.split(",")[0]).split("€")[1])
# print((product_price))
# print(type(product_price))

# Send the SMS
message_text = f"The {product_title} you are watching has a price of {product_price}\nActually, your target price is: {TARGET_PRICE}\nDifference from the target: {round(float((TARGET_PRICE) - product_price) * 1000)}€\nLink for purchase: {URL}"


def send_sms():
    client = Client(TWILLIO_SID, TWILLIO_AUTHTOKEN)
    message = client.messages.create(body=message_text, from_=MY_SENDING_NUMBER, to=MY_RECEIVING_NUMBER)


# Compare if the price of the product is equal to or below my target.
if product_price <= float(TARGET_PRICE):
    send_sms()
    print("sms sent")