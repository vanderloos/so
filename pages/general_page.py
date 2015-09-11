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

    def so_go_to_home_page(self):
        self.selenium.get(self.base_url)

    def so_go_to_page(self, url):
        self.selenium.get(self.base_url + url)

    def so_get(self, url):
        self.selenium.get(url)

    @property
    def so_window_handles(self):
        try:
            return self.selenium.window_handles
        except IndexError:
            return False

    @property
    def so_title(self):
        WebDriverWait(self, 10).until(lambda s: s.selenium.title)
        return self.selenium.title

    def so_maximize_window(self):
        self.selenium.maximize_window()

    def s0_is_attribute_present(self, element, attribute):
        self.selenium.implicitly_wait(0)
        try:
            element.get_attribute(attribute)
            return True
        except (NoSuchAttributeException, StaleElementReferenceException):
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def so_get_attribute(self, locator, attribute):
        try:
            return self.selenium.find_element(*locator).get_attribute(attribute)
        except (NoSuchAttributeException, StaleElementReferenceException, NoSuchElementException):
            return []

    def so_is_present(self, locator):
        try:
            self.selenium.find_element(locator)
            return True
        except NoSuchElementException:
            return False

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

    def so_find_elements(self, locator):
        try:
            return self.selenium.find_elements(*locator)
        except (NoSuchElementException, ElementNotVisibleException):
            return []

    def so_text(self, locator):
        try:
            return self.selenium.find_element(*locator).text
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            assert ("Element %s is not present" % str(locator))    

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

