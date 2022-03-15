import unittest
import aos_methods as methods

class AosAppPositiveTestCases(unittest.TestCase):   # create class

    @staticmethod  # signal to unit test that this is a static method
    def test_create_new_user():
        methods.setUp()
        # ------ CREATE NEW USER -------------
        methods.create_new_user()
        # ------- Validate Text Speaker, Tablets, Headphones, Laptops, Mice---------------
        methods.validate_text()
        # ------- Validate Top Menu bar Our Products, Special offer, popular items, contact us ------------
        methods.validate_top_menu()
        # --------- Verify the logo ------------
        methods.verify_logo_display()
        # -------- Validate Social Media Facebook, Twitter, and LindedIn---------------
        methods.validate_social_media()
        # -------- Validate Contact Us chatbox and form ------------
        methods.validate_contact_us()
        # -------- LOG OUT AS NEW USER -----------------
        methods.logout()
        # -------- LOGIN AS NEW USER -----------------
        methods.login()
        methods.logout()
        # -------------------------
        methods.teardown()

