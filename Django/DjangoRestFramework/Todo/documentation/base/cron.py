# from datetime import datetime, timedelta
# from django.utils import timezone
# from django_cron import CronJobBase, Schedule
# from .models import *
#
#
# def UserValidationCheck():
#     date = timezone.now()
#     users = CustomUser.objects.filter(is_verified = False)
#     print(users)
#     for user in users:
#         print(user)
#         if (date - user.date_joined)  > timedelta(days=1):
#             user.delete()
#
# def test():
#     print("Testing 121212")



# class UserValidationCheck(CronJobBase):
#     runtime_min = 1
#     schedule = Schedule(run_every_mins=runtime_min)
#     code = 'base.user_validation_check'
#     date = timezone.now()

#     def do(self):
#         print("start")
#         users = CustomUser.objects.filter(is_verified = False)
#         print(users)
#         for user in users:
#             print(user)
#             if (self.date - user.date_joined)  > timedelta(days=1):
#                 user.delete()
