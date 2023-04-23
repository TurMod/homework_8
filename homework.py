from datetime import datetime, timedelta



def get_birthdays_per_week(users: list) -> None:
    users_birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    today_date = datetime.now().date()
    today_weekday = today_date.weekday()
    next_monday = today_date + timedelta(days= 7 - today_weekday)
    next_friday = next_monday + timedelta(days=4)
    present_saturday = next_monday - timedelta(days=2)
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        weekday = datetime.strftime(birthday, '%A')
        if birthday >= next_monday and birthday <= next_friday:
            users_birthdays[weekday].append(name)
        elif birthday >= present_saturday and birthday < next_monday:
            users_birthdays['Monday'].append(name)
    for weekday, birthdays in users_birthdays.items():
        if birthdays:
            names_list = ', '.join(birthdays)
            print(f'{weekday}: {names_list}')


get_birthdays_per_week(
    [
        {'name': 'Buba', 'birthday': datetime(year=2023, month=4, day=24)},
        {'name': 'Chel', 'birthday': datetime(year=2023, month=4, day=27)},
        {'name': 'Michael', 'birthday': datetime(year=2023, month=4, day=23)},
        {'name': 'Raly', 'birthday': datetime(year=2023, month=4, day=29)}
    ]
)
