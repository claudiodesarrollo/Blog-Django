from django.urls import path
import pages
from . import views

urlpatterns = [
        path('pagina/<str:slug>',pages.views.page,name="page")
]
