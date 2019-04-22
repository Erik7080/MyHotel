from django.urls import path
from django.conf.urls import url
from mainapp import views


urlpatterns = [

    # No path specified
    path('', views.index, name='index'),
    # homepage
    path('homepage/', views.homepage, name='homepage'),
    # about
    path('about/', views.about, name='about'),
    # contact
    path('contact/', views.contact, name='contact'),
    # reservation
    path('reservation/', views.reservation, name='reservation'),
    # Ajax: filter available extras
    path('reservation/filtered/', views.filter, name='anything'),
    # Ajax: filter available extras
    path('reservation/filter_room_prices/', views.filter_room_prices, name='filter_room_prices'),
    # services
    path('services/', views.services, name='services'),
    # room_single
    path('room_single/', views.room_single, name='room_single'),
    # room_double
    path('room_double/', views.room_double, name='room_double'),
    # room_twin
    path('room_twin/', views.room_twin, name='room_twin'),
    # booking_confirm
    path('booking_confirm/', views.booking_confirm, name='booking_confirm'),
    # email_confirmed
    path('email_confirmed/', views.email_confirmed, name='email_confirmed'),
    # booking_completed
    path('booking_completed/', views.send_email, name='booking_completed'),

]