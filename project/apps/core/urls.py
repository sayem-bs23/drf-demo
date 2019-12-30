from django.conf.urls import url, include
from rest_framework import routers
from core.views import KeyvalueViewSet


router = routers.DefaultRouter()
router.register(r'values', KeyvalueViewSet)


urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
urlpatterns += router.urls

