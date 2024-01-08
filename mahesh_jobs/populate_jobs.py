import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mahesh_jobs.settings')
import django

django.setup()

from jobsApp.models import HydJobs, PuneJobs, BangJobs
from faker import Faker
from random import *


def phonenumbergen():
    d1 = randint(6, 9)
    num = '' + str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)


def populate(n, loc):
    for i in range(n):
        fake = Faker()
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=(
            'Project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer', 'Pyhton Web Developer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        # fake.phone_number() -> (844)604-1824x9158
        match (loc):
            case 1:
                HydJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility,
                                              email=femail, address=faddress, phonenumber=fphonenumber)
            case 2:
                BangJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility,
                                               email=femail, address=faddress, phonenumber=fphonenumber)
            case 3:
                PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility,
                                               email=femail, address=faddress, phonenumber=fphonenumber)
            case _:
                print(f'{n} records created successfully')


loc = int(input('Enter Location choice for inserting records- 1.Hyd 2.Bang 3.Pune '))
n = int(input('Enter number of records:'))
populate(n, loc)
print(f'{n} Records inserted successfully.....')
