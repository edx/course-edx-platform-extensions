# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import openedx.core.djangoapps.xmodule_django.models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSetting',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('id', openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, serialize=False, primary_key=True)),
                ('languages', models.TextField(help_text=b'A comma-separated list of language codes to release to the public.', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='courseaggregatedmetadata',
            name='id',
            field=openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, serialize=False, primary_key=True),
        ),
    ]
