# Generated by Django 3.1.4 on 2021-01-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_categorys', '0004_auto_20210107_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys_manytomanyfield',
            name='Article_id',
            field=models.IntegerField(blank=True, max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='categorys_manytomanyfield',
            name='Category_id',
            field=models.IntegerField(blank=True, max_length=999, null=True),
        ),
    ]