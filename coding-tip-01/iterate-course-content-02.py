# for versions of edx-platform Olive and later
# -----------------------------------------------------------------------------
from xmodule.modulestore.django import modulestore
from xmodule.modulestore import ModuleStoreEnum

# for older versions of edx-platform
# -----------------------------------------------------------------------------
from common.lib.xmodule.xmodule.modulestore.django import modulestore
from common.lib.xmodule.xmodule.modulestore import ModuleStoreEnum


from opaque_keys.edx.keys import CourseKey


def iterate_course_content(course_key: CourseKey):
    """
    Iterate every piece of content in a published course.
    """

    store = modulestore()

    with store.branch_setting(ModuleStoreEnum.Branch.published_only, course_key):
        course = store.get_course(course_key, depth=4)
        for chapter in course.get_children():
            for sequence in chapter.get_children():
                for vertical in sequence.get_children():
                    for child in vertical.get_children():
                        print("hello world!")
