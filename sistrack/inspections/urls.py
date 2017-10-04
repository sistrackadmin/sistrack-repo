from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.DeviceListView.as_view(), name='devices'),
    url(r'^device/(?P<pk>\d+)$', views.DeviceDetailView.as_view(), name='device-detail'),
]

urlpatterns += [
    url(r'^mytests/$', views.DeviceTestedByUserListView.as_view(), name='my-tests'),
]

urlpatterns += [
    url(r'^alltests/$', views.AllDevicesTestedListView.as_view(), name='all-tests'),
]
