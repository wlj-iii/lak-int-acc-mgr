# Generated by Django 3.2.5 on 2021-07-16 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0016_alter_device_device_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='asset_tag',
        ),
        migrations.RemoveField(
            model_name='device',
            name='imei_number',
        ),
        migrations.RemoveField(
            model_name='device',
            name='lan_mac_address',
        ),
        migrations.RemoveField(
            model_name='device',
            name='make_and_model',
        ),
        migrations.RemoveField(
            model_name='device',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='device',
            name='wlan_mac_address',
        ),
        migrations.AddField(
            model_name='device',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Manufacturer'),
        ),
        migrations.AddField(
            model_name='device',
            name='model_name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, verbose_name='Serial Number')),
                ('imei_number', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='IMEI Number')),
                ('lan_mac_address', models.CharField(blank=True, max_length=17, null=True, verbose_name='LAN MAC Address')),
                ('wlan_mac_address', models.CharField(blank=True, max_length=17, null=True, verbose_name='WLAN MAC Address')),
                ('asset_tag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.assettag')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.borrower')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
    ]
