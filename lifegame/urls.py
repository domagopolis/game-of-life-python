from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'lifegame'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ListView.as_view(), name='world-list'),
    url(r'^create/$', views.CreateView.as_view(), name='world-create'),
    url(r'^world/(?P<slug>[a-zA-Z0-9-]+)/$', views.DetailView.as_view(), name='world-detail'),
    url(r'^delete/(?P<slug>[a-zA-Z0-9-]+)/$', views.DeleteView.as_view(), name='world-delete'),
]
