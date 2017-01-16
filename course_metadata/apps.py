"""
app configuration
"""
from django.apps import AppConfig


class SolutionsAppCourseMetadataConfig(AppConfig):

    name = 'course_metadata'
    verbose_name = 'Course meta data'

    def ready(self):

        # import signal handlers
        import course_metadata.signals  # pylint: disable=unused-import
