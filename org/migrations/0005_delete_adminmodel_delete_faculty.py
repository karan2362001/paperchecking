# Generated by Django 4.2.10 on 2024-02-15 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("org", "0004_faculty"),
    ]

    operations = [
        migrations.DeleteModel(
            name="adminModel",
        ),
        migrations.DeleteModel(
            name="faculty",
        ),
    ]
