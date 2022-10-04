from model import controls
from model import pages


def test_form(setup_browser):

    pages.fill_fullname("Ivan", "Ivanov")
    pages.fill_user_email("ivan123@test.com")
    controls.select_gender_male()
    pages.fill_user_number_phone("5550001100")
    controls.select_date_of_birthday()
    pages.fill_subjects(("English", "Economics"))
    controls.select_hobby_music()
    controls.download_picture()
    pages.fill_current_address("Russia,Moscow")
    controls.select_state_and_city("Haryana", "Karnal")
    controls.submit()

    pages.check_data_in_table(
        [
            ('Student Name', 'Ivan Ivanov'),
            ('Student Email', 'ivan123@test.com'),
            ('Gender', 'Male'),
            ('Mobile', '5550001100'),
            ('Date of Birth', '25 January,1997'),
            ('Subjects', 'English, Economics'),
            ('Hobbies', 'Music'),
            ('Picture', 'file_1.jpg'),
            ('Address', 'Russia,Moscow'),
            ('State and City', 'Haryana Karnal')
        ]
    )
