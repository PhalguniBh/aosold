from faker import Faker
fake = Faker(locale='en_CA')
#------------------ locators section-------------------------------
app = 'AOS'
url = 'https://advantageonlineshopping.com/#/'
title = ' Advantage Shopping'
chatbox_title = 'Advantage Online Shopping Demo Support Chat'
facebook_url = 'https://www.facebook.com/MicroFocus/'
twitter_url = 'https://twitter.com/MicroFocus'
linkedin_url = 'https://www.linkedin.com/company/unavailable/'

curr_handle = ""

# data section
first_name = fake.first_name()
user_name = f'pb{first_name}'.lower().strip()
password = fake.password()
middle_name = fake.first_name()
last_name = fake.name()
full_name = first_name + last_name
email = f'{user_name}@{fake.free_email_domain()}'
phone = fake.phone_number()
city = fake.city()
state = 'Iovia'
address = fake.street_address().replace("\n", "")
postal_code = fake.postcode()

speaker_text = 'SPEAKERS'
tablet_text = 'TABLETS'
laptop_text = 'LAPTOPS'
mice_text = 'MICE'
headphones_txt = 'HEADPHONES'
subject_box = 'Hello there'

menu_item1 = "OUR PRODUCTS"
menu_item2 = 'SPECIAL OFFER'
menu_item3 = 'POPULAR ITEMS'
menu_item4 = 'CONTACT US'

list_ids = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
            'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
            'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
            'postal_codeRegisterPage']

list_val = [user_name, email, password, password, first_name, last_name, phone, city, address, state, postal_code]

