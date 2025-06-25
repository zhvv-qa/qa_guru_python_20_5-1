from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if time(hour=22) <= current_time or current_time <= time(hour=6):
        is_dark_theme = True
    elif time(hour=6) < current_time < time(hour=22):
        is_dark_theme = False
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is None:
        if time(hour=22) <= current_time or current_time <= time(hour=6):
            is_dark_theme = False
        else:
            is_dark_theme = True
        assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # найдите пользователя с именем "Olga"
    suitable_users = None

    for user in users:
        if user["name"] == "Olga":
            suitable_users = user
            break

    assert suitable_users == {"name": "Olga", "age": 45}

    # найдите всех пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] < 20]

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def print_readable_function_name(func, *args):
        func_name = func.__name__.replace('_', ' ').title()
        args_name = ", ".join([*args])
        print(f"{func_name} [{args_name}]")
        return f"{func_name} [{args_name}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_readable_function_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_readable_function_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_readable_function_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

def print_readable_function_name(func, *args):
        func_name = func.__name__.replace('_', ' ').title()
        args_name = ", ".join([*args])
        print(f"{func_name} [{args_name}]")
        return f"{func_name} [{args_name}]"