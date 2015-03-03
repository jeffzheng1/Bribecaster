# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_auto_20150302_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsfeedback',
            name='message_recieved_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 0, 6, 50, 225298)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsfeedback',
            name='message_sent_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 0, 6, 50, 225265)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsfeedback',
            name='sms_recieved_text',
            field=models.CharField(default=b'SMS Not Received', max_length=280),
            preserve_default=True,
        ),
    ]
