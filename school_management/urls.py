from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school_management.views import LeaderShipViewSet, SchoolStaffViewSet, GroupViewSet, SubjectViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'leaderships', LeaderShipViewSet)
router.register(r'school-staff', SchoolStaffViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
