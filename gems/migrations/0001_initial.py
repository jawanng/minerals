# Generated by Django 2.2.1 on 2019-05-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image_filename', models.CharField(max_length=120)),
                ('image_caption', models.CharField(blank=True, max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('formula', models.CharField(max_length=120)),
                ('strunz_classification', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120, null=True)),
                ('crystal_system', models.CharField(max_length=120, null=True)),
                ('unit_cell', models.CharField(max_length=120, null=True)),
                ('crystal_symmetry', models.CharField(max_length=120, null=True)),
                ('cleavage', models.CharField(max_length=120, null=True)),
                ('mohs_scale_hardness', models.CharField(max_length=120, null=True)),
                ('luster', models.CharField(max_length=120, null=True)),
                ('streak', models.CharField(max_length=120, null=True)),
                ('diaphaneity', models.CharField(max_length=120, null=True)),
                ('optical_properties', models.CharField(max_length=120, null=True)),
                ('refractive_index', models.CharField(max_length=120, null=True)),
                ('crystal_habit', models.CharField(max_length=120, null=True)),
                ('specific_gravity', models.CharField(max_length=120, null=True)),
                ('group', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
