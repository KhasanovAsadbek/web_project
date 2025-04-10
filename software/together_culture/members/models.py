from django.db import models

class Member(models.Model):
    MEMBERSHIP_TYPES = [
        ('CM', 'Community Member'),
        ('KA', 'Key Access Member'),
        ('CW', 'Creative Workspace Member'),
    ]
    INTERESTS = [
        ('caring', 'Caring'),
        ('sharing', 'Sharing'),
        ('creating', 'Creating'),
        ('experiencing', 'Experiencing'),
        ('working', 'Working'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_type = models.CharField(max_length=2, choices=MEMBERSHIP_TYPES)
    predominant_interest = models.CharField(max_length=20, choices=INTERESTS)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Visit(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    visit_date = models.DateField()

    def __str__(self):
        return f"{self.member.name} - {self.event.name}"
