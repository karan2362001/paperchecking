# Generated by Django 4.2.10 on 2024-02-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="adminModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("adminname", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("contact", models.PositiveIntegerField()),
                ("institutename", models.CharField(max_length=50)),
                ("institutecode", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=100)),
            ],
        ),
    ]
