import ast

from rest_framework import serializers
from openedx.core.lib.api.serializers import CourseKeyField
from course_metadata.models import CourseSetting


class StringListField(serializers.ListField):
    child = serializers.CharField(max_length=255)

    def to_representation(self, data):
        """
        List of object instances -> List of dicts of primitive datatypes.
        """
        if isinstance(data, basestring):
            data = ast.literal_eval(data)
        return data


class CourseSettingSerializer(serializers.ModelSerializer):
    id = CourseKeyField(required=False)
    languages = StringListField()

    class Meta:
        model = CourseSetting
