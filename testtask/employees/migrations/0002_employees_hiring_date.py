# Generated by Django 4.2.16 on 2024-10-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employees",
            name="hiring_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
