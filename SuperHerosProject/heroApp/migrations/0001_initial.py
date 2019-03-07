# Generated by Django 2.0.6 on 2019-03-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperHeroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=200)),
                ('contribution', models.CharField(choices=[('Rich', 'RICH'), ('Super Powers', 'SUPER POWERS')], max_length=2)),
                ('superPowers', models.CharField(choices=[('Flight', 'Flight'), ('Speed', 'Speed'), ('Invisibility', 'Invisibility'), ('Telekenetic', 'Telekenetic'), ('Healing', 'Healing'), ('Other', 'Other')], max_length=6)),
                ('you', models.CharField(choices=[('Good', 'Good'), ('Kinda Good', 'Kinda Good'), ('Neutral', 'Neutral'), ('A Little Evil', 'A Little Evil'), ('Evil', 'Evil')], max_length=5)),
                ('experience', models.TextField(default='', max_length=2000)),
            ],
        ),
    ]
