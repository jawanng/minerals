# Generated by Django 2.2.1 on 2019-05-25 17:38

from django.db import migrations
import json


def import_gems(apps, schema_editor):
    Gem = apps.get_model('gems', 'Gem')

    with open('minerals.json') as f:
        gems = json.load(f)

    for gem in gems:
        obj = Gem(**gem)
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_gems),
    ]
