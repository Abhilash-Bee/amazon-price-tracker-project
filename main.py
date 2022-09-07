import dotenv
from bs4 import BeautifulSoup
import requests
import smtplib
import os

dotenv.load_dotenv()

USER = os.getenv("REACT_APP_USER_ID")
PASSWORD = os.getenv("REACT_APP_PASSWORD")
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# response = requests.get(url="https://www.flipkart.com/apple-2022-macbook-pro-m2-8-gb-512-gb-ssd-mac-os-monterey-"
#                             "mnej3hn-a/p/itm16d048c105239?pid=COMGFB2GHYYUVJGF&lid=LSTCOMGFB2GHYYUVJGFISMUCW&marketplace"
#                             "=FLIPKART&q=macbook+pro+13&store=6bo%2Fb5g&srno=s_1_6&otracker=search&otracker1=search&fm"
#                             "=organic&iid=6ad41e17-737d-48b7-aea4-f2024f6ba9fc.COMGFB2GHYYUVJGF.SEARCH&ppt=hp&ppn="
#                             "homepage&ssid=4cqkvxv0o00000001662346241773&qH=e4731c954c776d06", headers=header)
# website_received = response.text
#
# soup = BeautifulSoup(website_received, "html.parser")
# print(soup.find(name="div", class_="_30jeq3 _16Jk6d").getText())


response = requests.get(url="https://www.amazon.in/STARQ-Washer-Bottle-Compatible-Adjustable/dp/B07P5QXKH5/ref=sr_1_19?"
                            "keywords=starq+awp2.8+2800+w+heavy+duty+200-330+bar+car+pressure+washer&qid=1662349504&"
                            "sprefix=starq+car+pressure+washer+%2Caps%2C250&sr=8-19", headers=header)
website_received = response.text

soup = BeautifulSoup(website_received, "html.parser")
actual_price = soup.find(name="span", class_="a-offscreen").getText()
actual_price = actual_price.replace("₹", "")
actual_price = actual_price.replace(",", "")
actual_price = float(actual_price)


if actual_price < 1600:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=USER,
            msg=f"Subject:Bee Price drop\n\nThe price has been dropped"
                f" for {actual_price}, 'Foam washer'."
        )
        print("Sent Successful")
else:
    print("Unsuccessful")
