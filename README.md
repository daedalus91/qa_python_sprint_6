# Автотесты для сервиса «Яндекс Самокат»

https://qa-scooter.praktikum-services.ru/

## Стек
Python 3.9+, pytest, Selenium, Allure, Firefox

## Структура
- `locators/` — локаторы страниц
- `pages/` — Page Object: `BasePage`, `MainPage`, `OrderPage`
- `tests/test_faq.py` — раскрытие ответов в «Вопросах о важном»
- `tests/test_order.py` — позитивный заказ: 2 набора данных × 2 точки входа (верхняя и нижняя кнопка)
- `tests/test_header.py` — логотипы «Самоката» и Яндекса
- `data.py` — URL и тестовые данные
- `allure_results/` — результаты прогона для Allure


## Запуск
    pip install -r requirements.txt
    pytest --clean-alluredir

## Отчёт
    allure serve allure_results
