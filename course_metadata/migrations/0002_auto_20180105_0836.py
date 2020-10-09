import django.utils.timezone
from django.db import migrations, models

import model_utils.fields
from opaque_keys.edx.django.models import CourseKeyField


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
                ('id', CourseKeyField(max_length=255, serialize=False, primary_key=True)),
                ('languages', models.TextField(help_text=b'A comma-separated list of language codes to release to the public.', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='courseaggregatedmetadata',
            name='id',
            field=CourseKeyField(max_length=255, serialize=False, primary_key=True),
        ),
    ]
