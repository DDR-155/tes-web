import requests

url = input("URL : ")

response = requests.get(url)

if response.status_code == 200:
    print(response.text)  # Menampilkan isi kode .php
else:
    print("Gagal mengambil kode .php")
