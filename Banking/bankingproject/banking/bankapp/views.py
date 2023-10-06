from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models
from .models import Application
from .forms import ApplicationForm


# Create your views here.
def demo(request):
    return render(request, 'index.html')


def status(request):
    return render(request, 'status.html')


def message_view(request):
    return render(request, "message.html")


def form_view(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Applicationform accepted")
            return redirect("bankapp:message_view")
    else:
        form = ApplicationForm()
    return render(request, 'form.html', {'form':form})
