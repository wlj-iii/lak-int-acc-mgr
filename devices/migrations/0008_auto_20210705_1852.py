# Generated by Django 3.2.5 on 2021-07-05 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_auto_20210705_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettag',
            name='tag_id',
            field=models.CharField(max_length=20, unique=True, verbose_name='Tag ID'),
        ),
        migrations.AlterField(
            model_name='device',
            name='asset_tag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.assettag', verbose_name='Asset Tag'),
        ),
        migrations.AlterField(
            model_name='device',
            name='imei_number',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='IMEI Number'),
        ),
        migrations.AlterField(
            model_name='device',
            name='lan_mac_address',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='LAN MAC Address'),
        ),
        migrations.AlterField(
            model_name='device',
            name='wlan_mac_address',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='WLAN MAC Address'),
        ),
    ]
