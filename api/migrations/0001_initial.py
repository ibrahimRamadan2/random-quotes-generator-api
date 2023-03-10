# Generated by Django 4.1.6 on 2023-02-11 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Author Name')),
            ],
        ),
        migrations.CreateModel(
            name='Qoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=200, verbose_name='quote')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qoutes', to='api.author')),
            ],
        ),
    ]
