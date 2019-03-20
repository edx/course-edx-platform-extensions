"""
Utility methods for course metadata app
"""
from django.conf import settings
from django.db.models import Q

from xmodule.modulestore.django import modulestore
from student.models import CourseEnrollment


def remove_orphans(course_key, detached_categories):
    from contentstore.views.item import _delete_orphans
    from xmodule.modulestore import ModuleStoreEnum

    _delete_orphans(
        course_key, ModuleStoreEnum.UserID.mgmt_command, True
    )


def get_course_leaf_nodes(course_key):
    """
    Get count of the leaf nodes with ability to exclude some categories
    """
    nodes = []
    detached_categories = getattr(settings, 'PROGRESS_DETACHED_CATEGORIES', [])
    store = modulestore()
    orphans = store.get_orphans(course_key)
    if orphans:
        remove_orphans(course_key, detached_categories)
    verticals = store.get_items(course_key, qualifiers={'category': 'vertical'})
    for vertical in verticals:
        if hasattr(vertical, 'children') and not is_progress_detached_vertical(vertical) and \
                vertical.location not in orphans:
            nodes.extend([unit for unit in vertical.children
                          if getattr(unit, 'category') not in detached_categories])
    return nodes


def is_progress_detached_vertical(vertical):
    """
    Returns boolean indicating if vertical is valid for progress calculations
    If a vertical has any children belonging to PROGRESS_DETACHED_VERTICAL_CATEGORIES
    it should be ignored for progress calculation
    """
    detached_vertical_categories = getattr(settings, 'PROGRESS_DETACHED_VERTICAL_CATEGORIES', [])
    if not hasattr(vertical, 'children'):
        vertical = modulestore().get_item(vertical, 1)
    for unit in vertical.children:
        if getattr(unit, 'category') in detached_vertical_categories:
            return True
    return False
