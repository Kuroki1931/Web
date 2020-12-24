from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include
from rest_framework import routers
from ap1.views import TaskViewSet, UserViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
]