# Generated by Django 3.2.4 on 2021-06-23 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_snacks_purchaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='snacks',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
