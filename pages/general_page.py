#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ErrorInResponseException
from selenium.webdriver.common.action_chains import ActionChains


class Page(object):
    '''Base class for all Pages'''

    def __init__(self, testsetup):
        '''Constructor'''
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    @property
    def so_title(self):
        WebDriverWait(self, 10).until(lambda s: s.selenium.title)
        return self.selenium.title

    def so_maximize_window(self):
        self.selenium.maximize_window()

    def so_is_displayed(self, locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            return False

    def so_find_element(self, locator):
        try:
            result = self.selenium.find_element(*locator)
            return result
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException, ErrorInResponseException):
            return None

    def so_text(self, locator):
       return self.selenium.find_element(*locator).text
        
    def so_send_keys(self, locator, value):
        if value == '' or value == [] or value is None or value == {} or value == ():
            return
        try:
            return self.selenium.find_element(*locator).send_keys(value)
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            assert ("Element %s is not present" % str(locator))

    def so_click(self, locator):
        return self.selenium.find_element(*locator).click()

    def so_clear(self, locator):
        return self.selenium.find_element(*locator).clear()

    def so_mouse_hover(self, locator):
        hover = ActionChains(self.selenium).move_to_element(locator)
        WebDriverWait(self.selenium, 1)
        hover.perform()
        WebDriverWait(self.selenium, 1)

    def so_wait_for_present(self, locator):
        WebDriverWait(self.selenium, self.timeout).until(EC.presence_of_element_located(locator),
                                                         'The element has not loaded.')

