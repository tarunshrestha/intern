from django.core.management.base import BaseCommand
from base.models import Test  # Ensure 'myapp' is replaced with your actual app name

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        data = ["Test", "Choice", "me"]
        try:
            for name in data:
                instance, created = Test.objects.get_or_create(name=name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created: {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Already exists: {name}'))
            self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
