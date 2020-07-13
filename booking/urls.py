"""URLs for the booking app."""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/$',
        views.BookingDetailView.as_view(),
        name='booking_detail'),
    url(r'^create/$',
        views.BookingCreateView.as_view(),
        name='booking_create'),
    url(r'^$', views.BookingListView.as_view(), name='booking_list'),
]
