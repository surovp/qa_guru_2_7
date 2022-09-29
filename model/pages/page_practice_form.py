from typing import Tuple
from selene.support.conditions import have
from selene.support.shared import browser


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


def check_data_form():
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element(".table-responsive").should(have.text("Ivan"))
    browser.element(".table-responsive").should(have.text("Ivanov"))
    browser.element(".table-responsive").should(have.text("ivan123@test.com"))
    browser.element(".table-responsive").should(have.text("Male"))
    browser.element(".table-responsive").should(have.text("5550001100"))
    browser.element(".table-responsive").should(have.text("25 January,1997"))
    browser.element(".table-responsive").should(have.text("English, Economics"))
    browser.element(".table-responsive").should(have.text("Music"))
    browser.element(".table-responsive").should(have.text("file_1.jpg"))
    browser.element(".table-responsive").should(have.text("Russia,Moscow"))
    browser.element(".table-responsive").should(have.text("Haryana"))
    browser.element(".table-responsive").should(have.text("Karnal"))
