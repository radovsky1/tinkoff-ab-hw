import hashlib
import random
import uuid

import pandas as pd
from faker import Faker

FAKE = Faker(locale='ru_RU')

COUNT = 2_000_000

DATA = {
    'id': [],
    'name': [],
    'email': [],
    'bio': [],
    'password': [],
    'last_login': [],
}


def generate():
    id = uuid.uuid4()
    name = FAKE.name()
    email = FAKE.email()
    bio = FAKE.text()
    password = hashlib.sha256(
        str(random.randint(1, 1_000_000)).encode()
    ).hexdigest()
    last_login = FAKE.date_time_between(start_date='-1y', end_date='now')

    DATA['id'].append(id)
    DATA['name'].append(name)
    DATA['email'].append(email)
    DATA['bio'].append(bio)
    DATA['password'].append(password)
    DATA['last_login'].append(last_login)


if __name__ == '__main__':
    for _ in range(COUNT):
        generate()

    df = pd.DataFrame(DATA)
    df.to_csv('user_data.csv', index=False)
