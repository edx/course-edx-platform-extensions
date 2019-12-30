from rest_framework import serializers
from openedx.core.lib.api.serializers import CourseKeyField
from course_metadata.models import CourseSetting


class CourseSettingSerializer(serializers.ModelSerializer):
    id = CourseKeyField(required=False)

    class Meta:
        model = CourseSetting
        fields = '__all__'
