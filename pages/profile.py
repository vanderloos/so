#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for Profile Settings page https://my.solidopinion.com/profile'''

from selenium.webdriver.common.by import By
from so.pages.general_page import Page
from so.pages.regions.header import Header


class ProfilePage(Page):
    _edit_profile_locator = (By.ID, "button-change")
    _editable_name_locator = (By.ID, "visible_name")
    _visible_name_locator = (By.ID, "text_visible_name")
    _save_button_locator = (By.ID, "go_save")
    _error_message_locator = (By.XPATH, '//*[@id="page_message"]/div[@class="alert alert-error"]/span')
    _success_message_locator = (By.XPATH, '//*[@id="page_message"]/div[@class="alert alert-success"]/span')

    def click_edit_button(self):
        self.so_click(self._edit_profile_locator)

    @property
    def header(self):
        return Header(self.testsetup)

    def fill_in_name(self, name):
        self.so_click(self._editable_name_locator)
        self.so_clear(self._editable_name_locator)
        self.so_send_keys(self._editable_name_locator, name)

    def click_save_button(self):
        self.so_click(self._save_button_locator)

    @property
    def is_saving_successful(self):
        return self.so_is_displayed(self._success_message_locator)

    @property
    def is_saving_error_present(self):
        return self.so_is_displayed(self._error_message_locator)

    @property
    def name_value(self):
        return self.so_text(self._visible_name_locator)





