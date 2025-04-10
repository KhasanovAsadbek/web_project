from django.core.management.base import BaseCommand
from members.models import Member, Event, Visit
from datetime import date

class Command(BaseCommand):
    help = 'Delete all data and insert initial data into the database'

    def handle(self, *args, **kwargs):
        # Delete all existing data
        Visit.objects.all().delete()
        Member.objects.all().delete()
        Event.objects.all().delete()

        # Create members
        members = [
            {'name': 'John Doe', 'email': 'john.doe@example.com', 'membership_type': 'CM', 'predominant_interest': 'creating'},
            {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'membership_type': 'KA', 'predominant_interest': 'sharing'},
            {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'membership_type': 'CW', 'predominant_interest': 'working'},
            {'name': 'Bob Brown', 'email': 'bob.brown@example.com', 'membership_type': 'CM', 'predominant_interest': 'experiencing'},
            {'name': 'Charlie Davis', 'email': 'charlie.davis@example.com', 'membership_type': 'KA', 'predominant_interest': 'caring'},
            {'name': 'Diana Evans', 'email': 'diana.evans@example.com', 'membership_type': 'CW', 'predominant_interest': 'creating'},
            {'name': 'Eve Foster', 'email': 'eve.foster@example.com', 'membership_type': 'CM', 'predominant_interest': 'sharing'},
            {'name': 'Frank Green', 'email': 'frank.green@example.com', 'membership_type': 'KA', 'predominant_interest': 'working'},
            {'name': 'Grace Harris', 'email': 'grace.harris@example.com', 'membership_type': 'CW', 'predominant_interest': 'experiencing'},
            {'name': 'Henry Irving', 'email': 'henry.irving@example.com', 'membership_type': 'CM', 'predominant_interest': 'caring'},
        ]

        for member_data in members:
            Member.objects.create(**member_data)

        # Create events
        events = [
            {'name': 'Creative Workshop 1', 'date': date(2025, 3, 22), 'description': 'A workshop for creative minds.'},
            {'name': 'Community Gathering 1', 'date': date(2025, 3, 23), 'description': 'A gathering for community members.'},
            {'name': 'Art Exhibition 1', 'date': date(2025, 4, 5), 'description': 'An exhibition showcasing local art.'},
            {'name': 'Music Festival 1', 'date': date(2025, 4, 12), 'description': 'A festival featuring local musicians.'},
            {'name': 'Tech Meetup 1', 'date': date(2025, 4, 19), 'description': 'A meetup for tech enthusiasts.'},
        ]

        for event_data in events:
            Event.objects.create(**event_data)

        # Create visits
        visits = [
            {'member': Member.objects.get(email='john.doe@example.com'), 'event': Event.objects.get(name='Creative Workshop 1'), 'visit_date': date(2025, 3, 22)},
            {'member': Member.objects.get(email='jane.smith@example.com'), 'event': Event.objects.get(name='Community Gathering 1'), 'visit_date': date(2025, 3, 23)},
            {'member': Member.objects.get(email='alice.johnson@example.com'), 'event': Event.objects.get(name='Art Exhibition 1'), 'visit_date': date(2025, 4, 5)},
            {'member': Member.objects.get(email='bob.brown@example.com'), 'event': Event.objects.get(name='Music Festival 1'), 'visit_date': date(2025, 4, 12)},
            {'member': Member.objects.get(email='charlie.davis@example.com'), 'event': Event.objects.get(name='Tech Meetup 1'), 'visit_date': date(2025, 4, 19)},
            {'member': Member.objects.get(email='diana.evans@example.com'), 'event': Event.objects.get(name='Creative Workshop 1'), 'visit_date': date(2025, 3, 22)},
            {'member': Member.objects.get(email='eve.foster@example.com'), 'event': Event.objects.get(name='Community Gathering 1'), 'visit_date': date(2025, 3, 23)},
            {'member': Member.objects.get(email='frank.green@example.com'), 'event': Event.objects.get(name='Art Exhibition 1'), 'visit_date': date(2025, 4, 5)},
            {'member': Member.objects.get(email='grace.harris@example.com'), 'event': Event.objects.get(name='Music Festival 1'), 'visit_date': date(2025, 4, 12)},
            {'member': Member.objects.get(email='henry.irving@example.com'), 'event': Event.objects.get(name='Tech Meetup 1'), 'visit_date': date(2025, 4, 19)},
        ]

        for visit_data in visits:
            Visit.objects.create(**visit_data)

        self.stdout.write(self.style.SUCCESS('Successfully deleted existing data and inserted initial data'))
