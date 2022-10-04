from typing import Tuple
from selene import have
from selene.support.shared import browser


def open_browser():
    browser.open('/automation-practice-form')


def fill_fullname(first_name: str, last_name: str):
    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)


def fill_user_email(email: str):
    browser.element("#userEmail").type(email)


def fill_user_number_phone(phone: str):
    browser.element("#userNumber").type(phone)


def fill_subjects(subjects: Tuple):
    for subject in subjects:
        browser.element("#subjectsInput").send_keys(subject).press_enter()


def fill_current_address(adress: str):
    browser.element("#currentAddress").type(adress)


def check_data_in_table(data):
    rows = browser.element('.modal-content').all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
