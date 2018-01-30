# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0002_auto_20180105_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesetting',
            name='languages',
        ),
    ]
