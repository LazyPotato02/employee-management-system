from django.urls import path

from web_store.base.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
