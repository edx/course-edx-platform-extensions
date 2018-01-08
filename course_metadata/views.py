from opaque_keys.edx.keys import CourseKey
from edx_solutions_api_integration.permissions import SecureRetrieveUpdateAPIView
from course_metadata.models import CourseSetting
from course_metadata.serializers import CourseSettingSerializer


class CourseSettingView(SecureRetrieveUpdateAPIView):
    """
    **Use Case**

        Create course settings

    **Example Requests**

        POST /api/server/courses_metadata/{course_id}/settings

    **Request Params**

        **POST**

        -id: course id
        -langauges: A comma-separated list of language codes. Example: ['it', 'de-at', 'es', 'pt-br']

    **Response Values**

        **POST**

        If the request is successful, the request returns an HTTP 200 "OK" response.
    """
    serializer_class = CourseSettingSerializer
    queryset = CourseSetting.objects.all()

    def get_object(self):
        course_id = CourseKey.from_string(self.kwargs['course_id'])
        setting, __ = CourseSetting.objects.get_or_create(id=course_id)
        return setting
