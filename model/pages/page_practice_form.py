from typing import Tuple
from selene import have
import allure
from selene.support.shared import browser


@allure.step("Вводим ФИО")
def fill_fullname(first_name: str, last_name: str):
    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)


@allure.step("Вводим Емэил")
def fill_user_email(email: str):
    browser.element("#userEmail").type(email)


@allure.step("Вводим мобильный номер")
def fill_user_number_phone(phone: str):
    browser.element("#userNumber").type(phone)


@allure.step("Выбираем предметы")
def fill_subjects(subjects: Tuple):
    for subject in subjects:
        browser.element("#subjectsInput").send_keys(subject).press_enter()


@allure.step("Вводим адрес")
def fill_current_address(adress: str):
    browser.element("#currentAddress").type(adress)


@allure.step("Проверяем введённые данные")
def check_data_in_table(data):
    rows = browser.element('.modal-content').all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
