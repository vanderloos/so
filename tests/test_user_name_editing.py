#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Test that logged in user can edit and save the 'Name' field in the profile settings.
'''
from time import sleep
import pytest
from unittestzero import Assert
from so.pages.login import Login, LoginPage
from so.pages.profile import ProfilePage
from so.data.name_strings import names


class TestNameEdit():
    @pytest.mark.nondestructive
    @pytest.mark.parametrize('name', names)
    def test_user_name_edit_save(self, mozwebqa, name):
        Login().login(mozwebqa, mozwebqa.credentials['User']['login'], mozwebqa.credentials['User']['password'])
        login_page = LoginPage(mozwebqa)
        Assert.false(login_page.is_error_message_displayed, 'Wrong login credentials entered')
        # Here should be some implicit wait for JS element while the logging in, but due to its unstable appearance...
        sleep(3)

        profile_page = ProfilePage(mozwebqa)

        Assert.true(profile_page.header.is_login_user_name_present)
        profile_page.click_edit_button()
        sleep(1)
        profile_page.fill_in_name(name)
        profile_page.click_save_button()
        Assert.true(profile_page.is_saving_successful, 'No success message')
        Assert.true(profile_page.name_value == name, 'The actual name: %s does not correspond to the entered one: %s'
                    % (profile_page.name_value, name))






