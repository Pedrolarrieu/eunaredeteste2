from django.contrib import admin
from .models import Task
from django.urls import reverse_lazy


admin.site.register(Task)
