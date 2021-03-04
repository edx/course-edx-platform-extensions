course-edx-platform-extensions
==============================

Notice: This repo will be archived in April 2021.
#######

course-edx-platform-extensions (``course_metadata``) is a Django application responsible for storing and caching aggregated metadata for a course.


Open edX Platform Integration
-----------------------------
1. Update the version of ``course-edx-platform-extensions`` in the appropriate requirements file (e.g. ``requirements/edx/custom.txt``).
2. Add ``course_metadata`` to the list of installed apps in ``common.py``.
3. Install ``course_metadata`` app via requirements file.

.. code-block:: bash

  $ pip install -r requirements/edx/custom.txt

4. (Optional) Run tests:

.. code-block:: bash

   $ python manage.py lms --settings test test course_metadata.tests

