# Generated by Django 4.1.6 on 2023-02-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_qoute_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='count',
            field=models.IntegerField(default=0, verbose_name='number of call Counts'),
        ),
    ]