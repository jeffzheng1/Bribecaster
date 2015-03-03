# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20150302_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsfeedback',
            name='sms_sent_text',
            field=models.CharField(default=b'SMS Not Sent', max_length=140),
            preserve_default=True,
        ),
    ]
