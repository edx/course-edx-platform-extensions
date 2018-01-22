"""
Models for course_metadata app
"""
import ast
from django.db import models

from model_utils.models import TimeStampedModel
from openedx.core.djangoapps.xmodule_django.models import CourseKeyField

from .utils import get_course_leaf_nodes


class CourseAggregatedMetaData(TimeStampedModel):
    """
    Model for storing and caching aggregated metadata about a course.

    This model contains aggregated metadata about a course such as
    total modules, total assessments.
    """
    id = CourseKeyField(primary_key=True, max_length=255)  # pylint: disable=invalid-name
    total_modules = models.IntegerField(default=0)
    total_assessments = models.IntegerField(default=0)

    @staticmethod
    def get_from_id(course_id):
        """
        Load a CourseAggregatedMetaData object for a given course ID.

        First, we try to load the CourseAggregatedMetaData from the database. If it
        doesn't exist, we create CourseAggregatedMetaData in the database for
        future use.

        Arguments:
            course_id (CourseKey): the ID of the course aggregated data to be loaded

        Returns:
            CourseAggregatedMetaData: aggregated data of the requested course
        """
        try:
            course_metadata = CourseAggregatedMetaData.objects.get(id=course_id)
        except CourseAggregatedMetaData.DoesNotExist:
            course_metadata = CourseAggregatedMetaData(id=course_id)
            course_metadata.total_assessments = len(get_course_leaf_nodes(course_id))
            course_metadata.save()
        return course_metadata


class CourseSetting(TimeStampedModel):
    """
    This model have custom course settings.
    """
    id = CourseKeyField(primary_key=True, max_length=255)
    languages = models.TextField(
        blank=True,
        help_text="A comma-separated list of language codes to release to the public."
    )

    @property
    def languages_list(self):
        if not self.languages:
            return []
        return ast.literal_eval(self.languages)
