# Generated by Django 5.1.1 on 2024-10-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
