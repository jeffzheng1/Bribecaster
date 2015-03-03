# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sms_selected', models.BooleanField(default=False)),
                ('robo_call_selected', models.BooleanField(default=False)),
                ('follow_up_selected', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('aadhaar_number', models.BigIntegerField(default=-1, max_length=12)),
                ('gender', models.CharField(max_length=20, choices=[(b'0', b'Male'), (b'1', b'Female'), (b'2', b'Decline to respond')])),
                ('date_of_birth', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OBCFormResponse',
            fields=[
                ('form_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cases.Form')),
                ('religion', models.CharField(max_length=40)),
                ('caste', models.CharField(max_length=40)),
                ('sub_caste', models.CharField(max_length=40)),
                ('issued_in_past', models.BooleanField(default=False)),
                ('education_certification_contains_caste', models.BooleanField(default=False)),
                ('caste_serial_number', models.CharField(max_length=40)),
                ('name_of_father', models.CharField(max_length=40)),
                ('name_of_mother', models.CharField(max_length=40)),
                ('name_of_husband', models.CharField(default=b'NA', max_length=40)),
                ('male_constitutional_posts', models.CharField(max_length=60)),
                ('male_designation', models.CharField(max_length=60)),
                ('male_scale_of_pay', models.CharField(max_length=60)),
                ('male_date_of_start', models.CharField(max_length=60)),
                ('male_date_of_finish', models.CharField(max_length=60)),
                ('female_constitutional_posts', models.CharField(max_length=60)),
                ('female_designation', models.CharField(max_length=60)),
                ('female_scale_of_pay', models.CharField(max_length=60)),
                ('female_date_of_start', models.CharField(max_length=60)),
                ('female_date_of_finish', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=('cases.form',),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_name', models.CharField(default=b'default Office', max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('office_head', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('speed_rating', models.IntegerField(default=-1)),
                ('cost_rating', models.IntegerField(default=-1)),
                ('quality_rating', models.IntegerField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficeVisit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_used', models.CharField(max_length=1, choices=[(b'0', b'fard'), (b'1', b'domicile'), (b'2', b'marriage'), (b'3', b'divorce')])),
                ('time_of_visit', models.DateTimeField(default=datetime.datetime(2015, 3, 2, 23, 25, 48, 397254))),
                ('case', models.ForeignKey(to='cases.Case')),
                ('citizen', models.ForeignKey(to='cases.Citizen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoboCallFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_response', models.CharField(default=b'OBC Certificate', max_length=40)),
                ('time_of_call', models.DateTimeField(default=datetime.datetime(2015, 3, 2, 23, 25, 48, 398193))),
                ('case', models.ForeignKey(to='cases.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMSFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_sent_time', models.DateTimeField()),
                ('message_recieved_time', models.DateTimeField()),
                ('sms_sent_text', models.CharField(default=b'Sent SMS', max_length=140)),
                ('sms_recieved_text', models.CharField(max_length=280)),
                ('sms_sentiment', models.IntegerField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('role', models.CharField(default=b'Unassigned', max_length=30)),
                ('employee_number', models.IntegerField()),
                ('office', models.ForeignKey(to='cases.Office')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='form',
            name='citizen',
            field=models.ForeignKey(to='cases.Citizen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='form',
            name='office_visit',
            field=models.ForeignKey(to='cases.OfficeVisit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='citizen',
            field=models.ForeignKey(default=1, to='cases.Citizen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='office',
            field=models.ForeignKey(default=1, to='cases.Office'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='sms_response',
            field=models.ForeignKey(to='cases.SMSFeedback'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ManyToManyField(default=[1], to='cases.User'),
            preserve_default=True,
        ),
    ]
