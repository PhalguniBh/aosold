from faker import Faker
fake = Faker(locale='en_CA')
#------------------ locators section-------------------------------
app = 'AOS'
url = 'https://advantageonlineshopping.com/#/'
title = ' Advantage Shopping'

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

list_ids = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
            'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
            'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
            'postal_codeRegisterPage']

list_val = [user_name, email, password, password, first_name, last_name, phone, city, address, state, postal_code]

