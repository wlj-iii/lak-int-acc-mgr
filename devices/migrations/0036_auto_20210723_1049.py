# Generated by Django 3.2.5 on 2021-07-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0035_auto_20210723_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfoentry',
            name='primary_phone_type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Mobile'), (1, 'Work'), (2, 'Home')], null=True, verbose_name='Primary Phone Number Type'),
        ),
        migrations.AlterField(
            model_name='contactinfoentry',
            name='secondary_phone_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Mobile'), (1, 'Work'), (2, 'Home')], null=True, verbose_name='Secondary Phone Number Type'),
        ),
    ]
