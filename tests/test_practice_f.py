from model import controls
from model import pages


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

    pages.check_data_form()
