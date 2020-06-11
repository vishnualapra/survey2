from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('survey', views.Survey, basename='survey')
router.register('choice', views.Choice, basename='choice')
router.register('result', views.Result, basename='result')
urlpatterns = router.urls
# urlpatterns += [
#     path('ping/', views.Ping.as_view()),
# ]