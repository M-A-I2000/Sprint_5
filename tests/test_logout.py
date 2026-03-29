from pages.profile_page import ProfilePage

class TestLogoutFunction:

    def test_logout_button_click_shows_login_form(self, authorized_user):
        page = ProfilePage(authorized_user)
        page.find_and_click_logout_button()
        login_button = page.login_button_wait()

        assert login_button.is_displayed()