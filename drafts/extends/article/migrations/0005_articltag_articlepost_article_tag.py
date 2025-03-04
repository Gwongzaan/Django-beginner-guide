# Generated by Django 5.1.3 on 2024-12-27 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articlepost',
            name='article_tag',
            field=models.ManyToManyField(blank=True, related_name='article_tag', to='article.articltag'),
        ),
    ]
