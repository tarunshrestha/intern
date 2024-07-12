from .models import *
import random


def my_scheduled_job():
  print("Working...........................................")
  

def auto_create_test():
  a = Test(name=str(random.randint(00, 100)))
  a.save()
  print(a.name)
  