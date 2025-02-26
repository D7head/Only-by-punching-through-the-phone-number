import requests
from bs4 import BeautifulSoup

def search_phone_number(phone_number):
  query = f'"{phone_number}"'
  url = f"https://www.google.com/search?q={query}"

  try:
    response = requests.get(url)
    response.raise_for_status() 

    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', class_='tF2Cxc')
    
    print(f"Результаты для номера {phone_number}:")
    if results:
        for result in results:
            try:
               link = result.find('a')['href']
               title = result.find('h3').text
               print(f"\t{title}: {link}")
            except:
                print("\tНе удалось получить информацию из этого результата.")

    else:
        print("\tНичего не найдено.")
  except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")

if __name__ == "__main__":
  phone_number = input("Введите номер телефона для поиска (в формате +7xxxxxxxxxx): ")
  search_phone_number(phone_number)