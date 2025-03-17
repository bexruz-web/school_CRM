from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school_management.views import LeaderShipViewSet, SchoolStaffViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'leadership', LeaderShipViewSet)
router.register(r'school-staff', SchoolStaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
