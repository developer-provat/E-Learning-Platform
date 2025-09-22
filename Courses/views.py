from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson
from .forms import CourseForm, LessonForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "courses/course_detail.html", {"course": course})

@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "courses/course_form.html", {"form": form})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, "courses/lesson_detail.html", {"lesson": lesson})
