from requests import get, post

# # Получение всех работ
# print(get('http://localhost:5000/api/jobs').json())
#
# # Корректное получение одной работы
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/2').json())
#
# # Ошибочный запрос на получение одной работы — неверный id
# print(get('http://localhost:5000/api/jobs/1234').json())
#
# # Ошибочный запрос на получение одной работы — строка
# print(get('http://localhost:5000/api/jobs/ghbdtn').json())

# Корректный POST-запрос
print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 132,
                 'team_leader': 12,
                 'job': 'Работа',
                 'work_size': 100,
                 'collaborators': '1, 2, 3',
                 'is_finished': False}).json())

# Некорректные POST-запросы
# Атрибут json - пуст
print(post('http://127.0.0.1:5000/api/jobs', json={}).json())

# Отсутствует атрибут json
print(post('http://127.0.0.1:5000/api/jobs', ).json())

# Переданы не все требуемые поля
print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 132,
                 'team_leader': 12}).json())

# Получение всех работ
print(get('http://localhost:5000/api/jobs').json())
