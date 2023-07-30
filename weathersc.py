from bs4 import BeautifulSoup
import requests
import time

url = "https://www.google.com/search?q=hava+durumu+dolunay+fatsa&sxsrf=AB5stBg9KORCty3-LO2xaTRn_oRGofaMlQ%3A1690661180972&ei=PHHFZOLrOs7jxc8Pq8uJmAM&ved=0ahUKEwji-YHZ27SAAxXOcfEDHatlAjMQ4dUDCA8&uact=5&oq=hava+durumu+dolunay+fatsa&gs_lp=Egxnd3Mtd2l6LXNlcnAiGWhhdmEgZHVydW11IGRvbHVuYXkgZmF0c2EyBBAjGCcyBBAjGCcyBRAAGIAEMgYQABgIGB4yBhAAGAgYHkiwCFDcBVjcBXACeAGQAQCYAXygAXyqAQMwLjG4AQPIAQD4AQHCAgcQIxiwAxgnwgIKEAAYRxjWBBiwA-IDBBgAIEGIBgGQBgk&sclient=gws-wiz-serp"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

maintitle = soup.find("div", class_="UQt4rd").text
title = soup.find("div", class_="wob_loc q8U8x").text
weather_type = soup.find("img", id="wob_tci").get("alt")
day = soup.find("div", class_="Z1VzSb").text
temperature_celsius = soup.find("span", id="wob_tm").text

while True:
    print(f"----- {maintitle} - {day} -----")
    print(f"Şehir: {title}")
    print(f"Hava Durumu: {weather_type}")
    print(f"Sıcaklık: {temperature_celsius}°C")

    exit = input("çıkış için q ya basın: ")

    if exit.lower() == "q":
        break
