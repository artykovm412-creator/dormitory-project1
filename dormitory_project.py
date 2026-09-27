import requests


BASE_URL = "https://inai-col1.fishrungames.com"


def get_student(student_id):
    url = f"{BASE_URL}/students/{student_id}"
    response = requests.get(url)

    print("Студент:", response.status_code)
    return response.json()


def get_building(building_number):
    url = f"{BASE_URL}/buildings/{building_number}"
    response = requests.get(url)

    print("Корпус:", response.status_code)
    return response.json()


def get_room(room_number):
    url = f"{BASE_URL}/rooms/{room_number}"
    response = requests.get(url)

    print("Комната:", response.status_code)
    return response.json()


# Пользователь вводит данные
student_id = int(input("Введите ID студента: "))
building_number = int(input("Введите номер корпуса: "))
room_number = int(input("Введите номер комнаты: "))


# Получаем данные через GET-запросы
student = get_student(student_id)
building = get_building(building_number)
room = get_room(room_number)


# Проверяем условия
reasons = []


# 1. Студент должен быть иногородним
if student["resident"] is not False:
    reasons.append("Студент является местным.")


# 2. Корпус должен быть предназначен для студентов
if building["forStudents"] is not True:
    reasons.append("Корпус не предназначен для студентов.")


# 3. Комната должна быть свободной
if room["available"] is not True:
    reasons.append("Комната занята.")


# Дополнительная проверка:
# номер комнаты должен соответствовать корпусу
if room_number // 100 != building_number:
    reasons.append("Эта комната находится в другом корпусе.")


# Результат
print()
print("========== РЕЗУЛЬТАТ ==========")

if len(reasons) == 0:
    print("Заявка одобрена!")
    print("Студент может заселиться.")
else:
    print("Заявка отклонена.")
    print("Причины:")

    for reason in reasons:
        print("-", reason)