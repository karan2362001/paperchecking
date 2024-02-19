# Generated by Django 4.2.10 on 2024-02-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_customuser_options_alter_customuser_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[("1", "Super admin"), ("2", "admin"), ("3", "Faculty")],
                max_length=20,
            ),
        ),
    ]