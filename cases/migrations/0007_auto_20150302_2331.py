# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20150302_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='sms_response',
            field=models.ForeignKey(default=1, to='cases.SMSFeedback'),
            preserve_default=True,
        ),
    ]
