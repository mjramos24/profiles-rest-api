###Mapping a URL to an API view in Django
from django.urls import path, include #used for including list of URLs

from rest_framework.routers import DefaultRouter

from profiles_api import views

#additional note: adds browsable API for all the other items register to our router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()), #apiview
    path('',include(router.urls))
]
