from django.core.management.base import BaseCommand
from bank_mandatory_app.models import Group


class Command(BaseCommand):
    def handle(self, **options):
        print('Provisioning ...')
        if not Group.objects.all():
            Group.objects.create(name='Platinum', value=90)
            Group.objects.create(name='Gold', value=75)
            Group.objects.create(name='Silver', value=50)
            Group.objects.create(name='Bronze', value=10)
