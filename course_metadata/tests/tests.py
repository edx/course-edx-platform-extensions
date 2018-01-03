"""
Tests for course_metadata app
"""
from django.core.urlresolvers import reverse
from edx_solutions_api_integration.test_utils import APIClientMixin
from mock_django import mock_signal_receiver

from xmodule.modulestore.django import SignalHandler
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory

from course_metadata.signals import course_publish_handler_in_course_metadata
from course_metadata.models import CourseAggregatedMetaData

from xmodule.modulestore.tests.django_utils import (
    ModuleStoreTestCase,
    TEST_DATA_SPLIT_MODULESTORE
)


class CoursesMetaDataTests(ModuleStoreTestCase):
    """ Test suite for Course Meta Data """

    MODULESTORE = TEST_DATA_SPLIT_MODULESTORE
    ENABLED_SIGNALS = ['course_published']

    def setUp(self):
        super(CoursesMetaDataTests, self).setUp()

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
            display_name=u"test subsection",
        )
        self.unit = ItemFactory.create(
            parent_location=self.sub_section.location,
            category="vertical",
            metadata={'graded': True, 'format': 'Homework'},
            display_name=u"test unit",
        )
        self.content_child1 = ItemFactory.create(
            category="html",
            parent_location=self.unit.location,
            data=self.test_data,
            display_name="Html component"
        )

    def test_course_aggregate_metadata_update_on_course_published(self):
        """
        Test course aggregate metadata update receiver is called on course_published signal
        and CourseAggregatedMetaData is updated
        """
        with mock_signal_receiver(SignalHandler.course_published,
                                  wraps=course_publish_handler_in_course_metadata) as receiver:
            self.assertEqual(receiver.call_count, 0)

            # adding new video unit to course should fire the signal
            ItemFactory.create(
                category="video",
                parent_location=self.unit.location,
                data=self.test_data,
                display_name="Video to test aggregates"
            )

            self.assertEqual(receiver.call_count, 1)
            total_assessments = CourseAggregatedMetaData.objects.get(id=self.course.id).total_assessments
            self.assertEqual(total_assessments, 2)

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
        super(CourseSettingTests, self).setUp()

        self.course = CourseFactory.create()
        self.course_settings_uri = reverse('additional-course-settings', kwargs={'course_id': unicode(self.course.id)})
        self.languages = ["it", "de-at", "es", "pt-br"]

    def test_course_settings_languages(self):
        """
        Test for setting/getting course languages from course settings
        """
        data = {"languages": self.languages}
        response = self.do_put(self.course_settings_uri, data)
        self.assertEqual(response.status_code, 200)

        response = self.do_get(self.course_settings_uri)
        self.assertEqual(response.status_code, 200)
        for language in response.data['languages']:
            self.assertIn(language, self.languages)

    def test_course_settings_update_languages(self):
        """
        Test for updating course languages in course settings
        """
        data = {"languages": self.languages}
        response = self.do_put(self.course_settings_uri, data)

        self.assertEqual(response.status_code, 200)
        for language in response.data['languages']:
            self.assertIn(language, self.languages)

        updated_languages = ["it", "de-at", "es"]
        data = {"languages": updated_languages}
        response = self.do_put(self.course_settings_uri, data)

        self.assertEqual(response.status_code, 200)
        for language in response.data['languages']:
            self.assertIn(language, self.languages)
