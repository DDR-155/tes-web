import requests
from bs4 import BeautifulSoup

# URL dari website yang ingin Anda analisis
url = input('url web : ')

# Mengirim permintaan HTTP GET ke website
response = requests.get(url)

# Memastikan permintaan berhasil
if response.status_code == 200:
    # Menggunakan BeautifulSoup untuk melakukan analisis HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Contoh: Mendapatkan judul halaman
    title = soup.title.string
    print("Judul halaman:", title)

    # Contoh: Mendapatkan semua tautan di halaman
    links = soup.find_all('a')
    for link in links:
        print("Tautan:", link.get('href'))
else:
    print("Permintaan tidak berhasil. Kode status:", response.status_code)
