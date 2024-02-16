# Generated by Django 4.2.10 on 2024-02-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_customuser_delete_adminmodel_delete_faculty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[(1, "Super Admin"), (2, "Admin"), (3, "Faculty")],
                max_length=20,
            ),
        ),
    ]