from django import forms
from .models import SuperHeroModel


SUPER_POWER_CHOICES = (
    ('Flight','Flight'),
    ('Speed','Speed'),
    ('Invisibility','Invisibility'),
    ('Telekenetic','Telekenetic'),
    ('Healing','Healing'),
    ('Other','Other'),
    ('N/A','N/A'),
)


class HeroForm(forms.ModelForm):
    class Meta:
        model = SuperHeroModel
        fields = "__all__"
        labels = {
            'city': 'City or Origin',
            'contribution':'Are you rich or have super powers?',
            'superPowers': 'If you have a super power, which ones?',
            'you': 'Which of the following describes you?',
            'experience': 'Give us 3 examples of when you used your super hero abilities.'

        }
        widgets = {
            'superPowers': forms.SelectMultiple(choices=SUPER_POWER_CHOICES)

        }
