# Generated by Django 3.2.5 on 2021-07-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0032_auto_20210723_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfoentry',
            name='primary_phone_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Work'), (2, 'Home'), (3, 'Mobile')], null=True, verbose_name='Primary Phone Number Type'),
        ),
        migrations.AlterField(
            model_name='contactinfoentry',
            name='secondary_phone_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Work'), (2, 'Home'), (3, 'Mobile')], null=True, verbose_name='Secondary Phone Number Type'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
