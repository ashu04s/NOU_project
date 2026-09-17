from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import tbl_session


def home(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)

            messages.success(
                request,
                "Login successfully"
            )

            return redirect("superadmindesh")

        messages.error(
            request,
            "Login failed"
        )

    return render(request, "login.html")


def superadmindesh(request):
    return render(request, "superadmin/deshboard.html")


def base(request):
    return render(request, "superadmin/base.html")


def students(request):
    return render(request, "superadmin/students.html")


def teachers(request):
    return render(request, "superadmin/teachers.html")


def add_session(request):

    if request.method == "POST":

        session_name = request.POST.get("session_name")
        status = request.POST.get("status")
        strt_date = request.POST.get("strt_date")
        end_date = request.POST.get("end_date")

        tbl_session.objects.create(
            session_name=session_name,
            status=status,
            strt_date=strt_date,
            end_date=end_date
        )

        messages.success(
            request,
            "Session added successfully"
        )

        return redirect("add_session")

    return render(
        request,
        "add_session.html"
    )