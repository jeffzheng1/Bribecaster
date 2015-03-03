# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20150302_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officevisit',
            name='time_of_visit',
        ),
        migrations.RemoveField(
            model_name='robocallfeedback',
            name='time_of_call',
        ),
    ]
