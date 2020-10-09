from course_metadata.models import CourseSetting
from openedx.core.lib.api.serializers import CourseKeyField
from rest_framework import serializers


class CourseSettingSerializer(serializers.ModelSerializer):
    id = CourseKeyField(required=False)

    class Meta:
        model = CourseSetting
        fields = '__all__'
