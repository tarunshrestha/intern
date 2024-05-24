import datetime
from django_cron import CronJobBase, Schedule
from .models import *


class UserValidationCheck(CronJobBase):
    run_time_min = 60
    schedule = Schedule(run_every_mins=run_time_min)
    code = 'base.user_validation_check'
    date = datetime.now()

    def do(self):
        users = CustomUser.objects.filter(is_valid = False)
        for user in users:
            if user.date_joined.month - self.date.month > 1 or user.date_joined.day - self.date.day > 1 :
                user.delete()