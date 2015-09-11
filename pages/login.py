#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for a login page https://my.solidopinion.com/signin'''

from selenium.webdriver.common.by import By
from so.pages.general_page import Page


class LoginPage(Page):

    _username_locator = (By.ID, 'email')
    _password_locator = (By.ID, 'password')
    _login_button_locator = (By.ID, "go_login_page")
    _error_message_locator = (By.CSS_SELECTOR, ".alert.alert-error")

    def enter_username(self,user_name):
        self.so_send_keys(self._username_locator, user_name)

    def enter_pass(self,user_pass):
        self.so_send_keys(self._password_locator, user_pass)

    def click_login_button(self):
        self.so_click(self._login_button_locator)

    @property
    def is_error_message_displayed(self):
        return self.so_is_displayed(self._error_message_locator)

    @property
    def error_message_text(self):
        return self.so_find_element(self._error_message_locator).text


class Login():
    def enter_creds(self, mozwebqa, name, pwd):
        login_page = LoginPage(mozwebqa)
        login_page.selenium.get(login_page.base_url + '/signin')
        login_page.so_maximize_window()
        login_page.enter_username(name)
        login_page.enter_pass(pwd)

    def login(self, mozwebqa, name, pwd):
        login_page = LoginPage(mozwebqa)
        self.enter_creds(mozwebqa, name, pwd)
        login_page.click_login_button()


