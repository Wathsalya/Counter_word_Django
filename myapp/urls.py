from django.urls import path

from myapp.views import MyView

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MyView.as_view(), name='my-view'),
    path('count/', views.count, name='count')
]