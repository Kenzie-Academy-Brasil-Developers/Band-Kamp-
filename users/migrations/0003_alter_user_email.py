# Generated by Django 4.1.4 on 2022-12-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_first_name_alter_user_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
