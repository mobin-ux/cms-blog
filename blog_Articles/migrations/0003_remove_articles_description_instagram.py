# Generated by Django 3.1.4 on 2021-01-02 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_Articles', '0002_articles_description_instagram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='description_instagram',
        ),
    ]