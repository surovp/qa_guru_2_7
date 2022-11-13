from selene import have
from model import controls
from model import pages
"test"


def test_form(open_and_close_form):

    pages.fill_fullname("Ivan", "Ivanov")
    pages.fill_user_email("ivan123@test.com")
    controls.select_gender_male()
    pages.fill_user_number_phone("5550001100")
    controls.fill_date_of_birthday("25 January,1997")
    pages.fill_subjects(("English", "Economics"))
    controls.select_hobby_music()
    controls.download_picture()
    pages.fill_curent_adress("Russia,Moscow")
    controls.select_state_and_city("Haryana", "Karnal")
    controls.submit()

    pages.table_result.should(have.text("Ivan"))
    pages.table_result.should(have.text("Ivanov"))
    pages.table_result.should(have.text("ivan123@test.com"))
    pages.table_result.should(have.text("Male"))
    pages.table_result.should(have.text("5550001100"))
    pages.table_result.should(have.text("25 January,1997"))
    pages.table_result.should(have.text("English, Economics"))
    pages.table_result.should(have.text("Music"))
    pages.table_result.should(have.text("file_1.jpg"))
    pages.table_result.should(have.text("Russia,Moscow"))
    pages.table_result.should(have.text("Haryana"))
    pages.table_result.should(have.text("Karnal"))
