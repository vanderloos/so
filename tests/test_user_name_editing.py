#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''
from time import sleep
import pytest
from unittestzero import Assert
from so.pages.login import Login
from so.pages.profile import ProfilePage
from so.data.name_strings import names


class TestNameEdit():
    @pytest.mark.nondestructive
    @pytest.mark.parametrize('name', names)
    def test_menu_items(self, mozwebqa, name):
        Login().login(mozwebqa, mozwebqa.credentials['User']['login'], mozwebqa.credentials['User']['password'])

        profile_page = ProfilePage(mozwebqa)
        sleep(3)
        Assert.true(profile_page.header.is_login_user_name_present)
        profile_page.click_edit_button()
        profile_page.fill_in_name(name)
        profile_page.click_save_button()
        Assert.false(profile_page.is_saving_error_present, 'Error message present')
        Assert.true(profile_page.is_saving_successful, 'No success message')
        Assert.true(profile_page.name_value == name, 'The name does not correspond to the entered one')






