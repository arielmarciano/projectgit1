import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter.settings')
import django
django.setup()


import random
from faker import Faker
from main_app.models import User, Tweet


fakegen = Faker()


def create_user():
  username  = fakegen.user_name()
  email     = fakegen.email()
  return User.objects.get_or_create(username=username, email=email)[0]


def create_tweet(user):
  text  = fakegen.text(max_nb_chars=140)
  date  = fakegen.date()
  tweet = Tweet.objects.get_or_create(text=text, user=user, date=date)[0]


def populate():
  users = []
  for user in range(20):
    user = create_user()
    for tweet in range(50):
      tweet = create_tweet(user)


if __name__ == '__main__':
  print('Starting to populate...')
  populate()
  print('Finished populating!')









