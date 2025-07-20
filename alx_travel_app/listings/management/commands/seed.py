from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()

        locations = ['Kigali', 'New York', 'London', 'Paris', 'Nairobi']
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i+1}",
                description="This is a great place to stay!",
                price_per_night=random.randint(50, 300),
                location=random.choice(locations),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('✅ Seeded database with sample listings'))
