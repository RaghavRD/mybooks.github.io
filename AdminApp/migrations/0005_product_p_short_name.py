# Generated by Django 4.1.2 on 2022-12-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminApp", "0004_paymentmaster"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="p_short_name",
            field=models.CharField(default=11, max_length=30),
            preserve_default=False,
        ),
    ]
