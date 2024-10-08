# Generated by Django 5.1.1 on 2024-09-25 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription_course",
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
