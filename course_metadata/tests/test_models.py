"""
Tests for course_metadata app
"""
from django.core.urlresolvers import reverse

from course_metadata.models import CourseAggregatedMetaData
from edx_solutions_api_integration.test_utils import APIClientMixin
from xmodule.modulestore.tests.django_utils import (
    TEST_DATA_SPLIT_MODULESTORE, ModuleStoreTestCase)
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory


class CoursesMetaDataTests(ModuleStoreTestCase):
    """ Test suite for Course Meta Data """

    MODULESTORE = TEST_DATA_SPLIT_MODULESTORE
    ENABLED_SIGNALS = ['course_published']

    def setUp(self):
        super().setUp()

        self.course = CourseFactory.create()
        self.test_data = '<html>Test data</html>'

        self.chapter = ItemFactory.create(
            category="chapter",
            parent_location=self.course.location,
            display_name="Overview",
        )
        self.sub_section = ItemFactory.create(
            parent_location=self.chapter.location,
            category="sequential",
            display_name="test subsection",
        )
        self.unit = ItemFactory.create(
            parent_location=self.sub_section.location,
            category="vertical",
            metadata={'graded': True, 'format': 'Homework'},
            display_name="test unit",
        )
        self.content_child1 = ItemFactory.create(
            category="html",
            parent_location=self.unit.location,
            data=self.test_data,
            display_name="Html component"
        )

    def test_get_course_aggregate_metadata_by_course_key(self):
        """
        Test course aggregate metadata should compute and return metadata
        when called by get_from_id
        """
        course_metadata = CourseAggregatedMetaData.get_from_id(self.course.id)
        self.assertEqual(course_metadata.total_assessments, 1)


class CourseSettingTests(ModuleStoreTestCase, APIClientMixin):
    """ Test suite for Course Setting """

    MODULESTORE = TEST_DATA_SPLIT_MODULESTORE

    def setUp(self):
        super().setUp()

        self.course = CourseFactory.create()
        self.course_settings_uri = reverse('additional-course-settings', kwargs={'course_id': str(self.course.id)})

    def test_course_settings_get(self):
        """
        Test for getting settings
        """
        response = self.do_get(self.course_settings_uri)
        self.assertEqual(response.status_code, 200)
