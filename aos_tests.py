import unittest
from aos import aos_methods as methods


class AosTestPositiveTestCase(unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.set_up()
        methods.create_new_user()
        methods.log_in()
        methods.log_out()
        methods.main_logo()
        methods.checking_homepage_texts()
        methods.top_menu_clickable()
        methods.contactus()
        methods.tear_down()