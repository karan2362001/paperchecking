# Generated by Django 4.2.10 on 2024-02-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("org", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminmodel",
            name="contact",
            field=models.IntegerField(),
        ),
    ]