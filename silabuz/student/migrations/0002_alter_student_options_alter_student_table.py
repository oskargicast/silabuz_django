# Generated by Django 4.1.3 on 2022-11-18 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'student'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]