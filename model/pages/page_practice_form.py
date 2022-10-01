from typing import Tuple
from selene.support.shared import browser

table_result = browser.element(".table-responsive")


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


def fill_curent_adress(adress: str):
    browser.element("#currentAddress").type(adress)
