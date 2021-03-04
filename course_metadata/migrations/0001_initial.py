import django.utils.timezone
from django.db import migrations, models

import model_utils.fields
from opaque_keys.edx.django.models import CourseKeyField


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAggregatedMetaData',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('id', CourseKeyField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('total_modules', models.IntegerField(default=0)),
                ('total_assessments', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
