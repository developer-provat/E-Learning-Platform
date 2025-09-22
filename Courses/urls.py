from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
    path("course/new/", views.course_create, name="course_create"),
    path("lesson/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
]