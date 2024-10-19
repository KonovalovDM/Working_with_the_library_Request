# Задание 2: Параметры запрос
# 1. Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# 3. Распечатайте полученные записи.

import requests
import pprint

params = {
    'userId' : '1'
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

response_json = response.json()
pprint.pprint(response_json)

print(f'статус код: {response.status_code}')
if  response.status_code == 200:
    print('Запрос выполнен успешно')
else:
    print('Произошла ошибка')








# Задание 3: Отправка данных
# 1. Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# 2. Создайте словарь с данными для отправки (например, `{'title': 'foo', 'body': 'bar', 'userId': 1}`).
# 3. Отправьте POST-запрос с этими данными.
# 4. Распечатайте статус-код и содержимое ответа.
