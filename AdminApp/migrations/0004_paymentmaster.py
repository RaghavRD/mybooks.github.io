# Generated by Django 4.1.2 on 2022-12-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminApp", "0003_userinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentMaster",
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
                ("cardno", models.CharField(max_length=20)),
                ("cvv", models.CharField(max_length=4)),
                ("expiry", models.CharField(max_length=20)),
                ("balance", models.FloatField(default=50000)),
            ],
            options={
                "db_table": "PaymentMaster",
            },
        ),
    ]
