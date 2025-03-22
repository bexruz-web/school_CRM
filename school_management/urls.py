from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school_management.views import (LeaderShipViewSet, SchoolStaffViewSet, GroupViewSet, SubjectViewSet, ClubScheduleViewSet,
                                     TeacherViewSet, StudentViewSet, ScheduleViewSet, BellScheduleViewSet)
router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'leaderships', LeaderShipViewSet)
router.register(r'school-staff', SchoolStaffViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'bell-schedules', BellScheduleViewSet)
router.register(r'club-schedules', ClubScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
