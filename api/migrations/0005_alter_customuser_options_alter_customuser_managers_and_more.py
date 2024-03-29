# Generated by Django 4.2.10 on 2024-02-16 11:02

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_customuser_role"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="customuser",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[(1, "Super admin"), (2, "admin"), (3, "Faculty")],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
