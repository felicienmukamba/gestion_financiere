# Generated by Django 4.2.17 on 2024-12-09 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0004_besoin_etatbesoin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="date",
        ),
    ]