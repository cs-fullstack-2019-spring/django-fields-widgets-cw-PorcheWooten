from django.db import models

# Create your models here.

# Name
# City or Origin
# Are you rich or have super powers?
# If you have a super power, which ones? (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
# Which of the following are you? (Good, kinda good, neutral, a little evil, evil)
# Give us 3 example"s of when you used your super hero abilities.
CONTRIBUTION_CHOICES = (
    ('Rich','RICH'),
    ('Super Powers','SUPER POWERS'),
)


YOU_CHOICES = (
    ('Good','Good'),
    ('Kinda Good','Kinda Good'),
    ('Neutral','Neutral'),
    ('A Little Evil','A Little Evil'),
    ('Evil','Evil'),
)

class SuperHeroModel(models.Model):
    name = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    contribution = models.CharField(max_length=200, choices=CONTRIBUTION_CHOICES)
    superPowers = models.CharField(max_length=200)
    you = models.CharField(max_length=5000, choices=YOU_CHOICES)
    experience = models.TextField(max_length=2000, default="")