import requests
import pprint

# 1. Импортируйте библиотеку `requests`.
# 2. Отправьте GET-запрос к открытому API (например, [https://api.github.com](https://api.github.com/)) с параметром для поиска репозиториев с кодом html.
# 3. Распечатайте статус-код ответа.
# 4. Распечатайте содержимое ответа в формате JSON.

params = {
    'q' : 'html'
}

response = requests.get("https://api.github.com/search/repositories", params=params)

response_json = response.json()
pprint.pprint(response_json)

print(f'статус код: {response.status_code}')
if  response.status_code == 200:
    print('Запрос выполнен успешно')
else:
    print('Произошла ошибка')

print(f"Количество репозиториев с использованием html: {response_json['total_count']:,}")


