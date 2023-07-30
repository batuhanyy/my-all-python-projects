from bs4 import BeautifulSoup
import requests

while True:
    song_name = input("Lütfen şarkı ismini yazın (Çıkmak için 'q' tuşuna basabilirsiniz): ")
    if song_name.lower() == 'q':
        break

    search_query = song_name.replace(" ", "+")
    url = f"https://www.google.com/search?q={search_query}+lyrics"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    lyrics = soup2.find("div", class_="sATSHe").get_text()
    title = soup2.find("div", class_="PZPZlf ssJ7i B5dxMb").get_text()

    print("----- Şarkı Başlığı -----")
    print(title)
    print("----- Şarkı Sözleri -----")
    print(lyrics)

    file_name = f"{song_name}.txt"  # Şarkı adını dosya adı olarak kullan

    with open(file_name, "w") as file:
        file.write(title + "\n")
        file.write(lyrics + "\n")
