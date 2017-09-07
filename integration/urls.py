from django.conf.urls import url

from . import views
from . import views_student as student
from . import views_staff as staff


urlpatterns = [
    url(r'^onboarding/$', student.Onboard.as_view(), name='onboarding'),
    url(r'^account/$', student.AccountDetails.as_view(), name='account'),
    url(r'^sepa/(?P<pk>.+)/$', student.ContactSEPA.as_view(), name='contact_sepa'),
    url(r'^attachment/(?P<att_id>.+)/$', student.DownloadAttachment.as_view(), name='download_attachment'),

    url(r'^review/(?P<uuid>.+)/(?P<action>(confirm)|(discard))/$',
        staff.FileUploadAction.as_view(), name='upload_action'),
    url(r'^review/(?P<uuid>.+)/$', staff.FileUploadReview.as_view(), name='upload_review'),
    url(r'^student/(?P<pk>.+)/$', staff.StudentReview.as_view(), name='student_review'),
    url(r'^bulk/$', staff.BulkActions.as_view(), name='students_bulk'),
    url(r'^university/$', staff.DashboardUniversity.as_view(), name='university'),
    url(r'^courses/$', staff.DashboardCourses.as_view(), name='courses'),

    url(r'^$',
        views.dispatch_by_user(
            student.Dashboard.as_view(),
            staff.DashboardHome.as_view()),
        name='dashboard'),
]
