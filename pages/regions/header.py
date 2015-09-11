#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for a common page of www.lidtmere.dk site'''

from selenium.webdriver.common.by import By
from so.pages.general_page import Page

class Header(Page):
    """
    Page Object for pages header with menu
    """

    _bm_logo_locator = (By.CLASS_NAME, "logo")
    _logout_locator = (By.LINK_TEXT, "Log out")
    _menu_locator = (By.ID, "user_name")
    _menu_item_locator = (By.XPATH, "//*[@id='dropdownu-menu']/li/a")
    _login_user_name_locator = (By.ID, "user_name")

    def logout(self):
        self.so_click(self._menu_locator)
        self.so_click(self._logout_locator)

    def click_menu(self):
        self.so_click(self._menu_locator)

    @property
    def is_login_user_name_present(self):
        return self.so_is_displayed(self._login_user_name_locator)

    @property
    def login_user_name(self):
        return self.so_text(self._login_user_name_locator)

    @property
    def menu_items_list(self):
        menu_list = [menu_item_web_el.text for menu_item_web_el in self.so_find_elements(self._menu_item_locator)]
        return menu_list

