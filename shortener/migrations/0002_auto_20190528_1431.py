# Generated by Django 2.2.1 on 2019-05-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlprofile',
            name='default_lifespan',
            field=models.IntegerField(default=120, null=True),
        ),
        migrations.AlterField(
            model_name='urlprofile',
            name='default_max_uses',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='urlprofile',
            name='enabled',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='urlprofile',
            name='max_concurrent_urls',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AlterField(
            model_name='urlprofile',
            name='max_urls',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]
