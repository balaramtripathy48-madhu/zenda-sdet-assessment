from faker import Faker
import uuid

fake = Faker()

SIGNUP_NAME = fake.name()

def generate_unique_email():
    return f"zenda_{uuid.uuid4().hex[:12]}@example.com"

SIGNUP_PASSWORD = "TestPass123!"

FIRST_NAME = fake.first_name()
LAST_NAME = fake.last_name()
ADDRESS = "123 Test Street"
COUNTRY = "India"
STATE = "Karnataka"
CITY = "Bengaluru"
ZIPCODE = "560001"
MOBILE = "9876543210"