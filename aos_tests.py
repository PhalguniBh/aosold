import unittest
import aos_locators as locators
import aos_methods as methods

# class AosAppPositiveTestCases(unittest.TestCase):   # create class
#
#     @staticmethod   # signal to unit test that this is a static method
#     def test_create_new_user():
#         methods.setUp()
#         # ------ CREATE NEW USER -------------
#         methods.create_new_user()
#         methods.log_out()
#         # -------- LOGIN AS NEW USER -----------------
#         methods.login()
#         methods.log_out()
#         # --------------------------------------------
#         methods.teardown()


class AosAppPositiveTestCases(unittest.TestCase):   # create class

    @staticmethod  # signal to unit test that this is a static method
    def test_create_new_user(self=None):
        methods.setUp()
        # ------ CREATE NEW USER -------------
        methods.create_new_user()
        # -------- LOG OUT AS NEW USER -----------------
        methods.logout()
        # -------- LOGIN AS NEW USER -----------------
        methods.login()
        methods.logout()
        # -------------------------
        methods.teardown()
