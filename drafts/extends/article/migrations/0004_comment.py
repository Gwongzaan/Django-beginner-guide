# Generated by Django 5.1.3 on 2024-12-20 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articlepost_users_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.articlepost')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
