# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-26 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confreg', '0071_confreglog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencesession',
            name='lastnotifiedstatus',
            field=models.IntegerField(choices=[(0, 'Submitted'), (1, 'Approved'), (2, 'Not Accepted'), (3, 'Pending'), (4, 'Reserve'), (5, 'Pending reserve'), (6, 'Withdrawn')], default=0),
        ),
        migrations.AlterField(
            model_name='conferencesession',
            name='status',
            field=models.IntegerField(choices=[(0, 'Submitted'), (1, 'Approved'), (2, 'Not Accepted'), (3, 'Pending'), (4, 'Reserve'), (5, 'Pending reserve'), (6, 'Withdrawn')], default=0),
        ),
        migrations.RunSQL("""WITH t(id, statustext, statusgroup) AS (VALUES
        (0, 'Submitted', NULL),
        (1, 'Approved', 'Approved+Pending'),
        (2, 'Not accepted', NULL),
        (3, 'Pending', 'Approved+Pending'),
        (4, 'Reserve', 'Reserve+Pending'),
        (5, 'Pending reserve', 'Reserve+Pending'),
        (6, 'Withdrawn', NULL))
        INSERT INTO confreg_status_strings (id, statustext, statusgroup)
        SELECT id, statustext, statusgroup FROM t ON CONFLICT (id) DO UPDATE SET statustext=excluded.statustext, statusgroup=excluded.statusgroup""")

    ]