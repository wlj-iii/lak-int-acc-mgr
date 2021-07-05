# Generated by Django 3.2.5 on 2021-07-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_auto_20210705_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='device',
            name='model',
        ),
        migrations.AddField(
            model_name='device',
            name='make_and_model',
            field=models.PositiveSmallIntegerField(choices=[(100, 'Choose Device Make - Model'), (99, 'HP - Chromebook 11A G8 EE (USB-C charger)'), (98, 'Dell - Chromebook 3100 (USB-C charger)'), (97, 'HP - Chromebook 11-v031nr (AC Adapter, blue-tip plug)'), (96, 'Apple - iPad mini (1st Gen, Model A1432)'), (95, 'Apple - iPad mini 2 (2nd Gen, Model A1489)'), (94, 'Lenovo - 300e (2nd Gen.)'), (93, 'Lenovo - ThinkPad L450'), (92, 'Lenovo - ThinkPad L540'), (91, 'HP - ProDesk 400 G6 SFF (Lab-grade PC)'), (90, 'HP - ProDesk 600 G5 SFF (Teacher-grade PC)'), (89, 'Dell - OptiPlex 3020 (Teacher-grade PC)'), (88, 'Apple - iPad (6th Gen, Model A1893)'), (87, 'Apple - iPad (8th Gen, Model A2270)')], default=100, verbose_name='Make & Model'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Select Device Type'), (2, 'Desktop PC'), (3, 'Laptop PC (>=8GB RAM)'), (4, 'Laptop Charger'), (5, 'Notebook PC (<8GB RAM)'), (6, 'Notebook Charger'), (7, 'Tablet'), (8, 'Tablet Charger'), (9, 'WiFi Hotspot'), (10, 'Projector'), (11, 'IP Phone'), (12, 'Document Camera'), (13, 'High-Def TV'), (14, 'Swivl'), (15, 'Drone'), (16, 'Tri-Pod Stand')], default=1, verbose_name='Device Type'),
        ),
    ]
