# Generated by Django 5.1.1 on 2024-09-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="payment_url",
            field=models.URLField(
                blank=True, max_length=450, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="ID сессии"
            ),
        ),
    ]
