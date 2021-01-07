# Generated by Django 3.1.4 on 2021-01-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=999, null=True)),
                ('title', models.CharField(blank=True, max_length=999, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Image_Of_Articles')),
                ('CreationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('ReleaseStatus', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]