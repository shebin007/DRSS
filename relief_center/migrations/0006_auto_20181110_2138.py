# Generated by Django 2.1.3 on 2018-11-10 16:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('relief_center', '0005_auto_20181110_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reliefcenter',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
    ]
