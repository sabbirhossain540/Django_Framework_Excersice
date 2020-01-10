import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','experement_project.settings')

import django
django.setup()

#Fake POP Script
import random
from test_app.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name().split()
        fake_firstName = fake_name[0]
        fake_lastName = fake_name[1]
        fake_email = fakegen.email()

    user = User.objects.get_or_create(first_name=fake_firstName,last_name=fake_lastName,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populate Complete")
