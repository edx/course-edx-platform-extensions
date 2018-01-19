import ast

from rest_framework import serializers
from openedx.core.lib.api.serializers import CourseKeyField
from course_metadata.models import CourseSetting


class StringListField(serializers.ListField):
    child = serializers.CharField(max_length=255)

    def to_representation(self, data):
        """
        Parse a string into a python list. Converts empty string to empty list.
        If data is already a list then no operation is performed on that data.
        """
        if not data:
            return []

        if isinstance(data, basestring):
            data = ast.literal_eval(data)
        return data


class CourseSettingSerializer(serializers.ModelSerializer):
    id = CourseKeyField(required=False)
    languages = StringListField()

    class Meta:
        model = CourseSetting
