import unittest
import aos_methods as methods
from time import sleep

class AosAppPositiveTestCases(unittest.TestCase):   # create class

    # @staticmethod  # signal to unit test that this is a static method
    def test_create_new_user(self):
        methods.setUp()
        # ------ CREATE NEW USER -------------
        sleep(0.25)
        methods.create_new_user()
        # ------- Validate Text Speaker, Tablets, Headphones, Laptops, Mice---------------
        sleep(0.25)
        methods.validate_text()
        # ------- Validate Top Menu bar Our Products, Special offer, popular items, contact us ------------
        sleep(0.25)
        methods.validate_top_menu()
        # --------- Verify the logo ------------
        sleep(0.25)
        methods.verify_logo_display()
        # -------- Validate Social Media Facebook, Twitter, and LindedIn---------------
        sleep(0.25)
        methods.validate_social_media()
        # -------- Validate Contact Us chatbox and form ------------
        sleep(0.25)
        methods.validate_contact_us()
        # -------- LOG OUT AS NEW USER -----------------
        sleep(0.25)
        methods.logout()
        # -------- LOGIN AS NEW USER -----------------
        sleep(0.25)
        methods.login()
        # --------Shopping cart checkout functionality  validation ---------------
        sleep(0.25)
        methods.validate_add_itemto_shopping_cart()
        #----------Validate no order is displayed -------
        sleep(0.25)
        methods.validate_no_order()
        sleep(0.25)
        methods.logout()
        # -------------------------
        sleep(0.25)
        methods.teardown()
