# Generated by Django 4.2.10 on 2024-02-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("org", "0002_alter_adminmodel_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminmodel",
            name="adminname",
            field=models.CharField(max_length=50),
        ),
    ]
