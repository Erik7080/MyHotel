from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import datetime
from mainapp.models import RoomType, Extra
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.http import JsonResponse
import json

appname = 'MyHotel'


def index(request):

    room_type = retrieve_room_types()  # Retrieve all the rooms
    today = datetime.date.today()  # Retrieve today day
    addition_day = datetime.timedelta(days=1)  # add to any date 1
    day_after = datetime.date.today() + addition_day  # the day after today
    today_format = today.strftime('%d/%m/%y')  # today in the correct format
    day_after_format = day_after.strftime('%d/%m/%y') # tomorrow in the correct format
    nights = day_after - today  # calculate the nights

    dict = {
        'rooms': room_type,
        'tday' : today_format,
        'day_after': day_after_format,
        'nights': nights,

    }
    return render(request, 'mainapp/index.html', context= dict)


def send_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['fullname']
        final_body = 'Dear ' + name + ',''\n''\n''Congratulations, Your booking at MyHotel - London is complete.' '\n''\n'\
                                           'Do not hesitate to let us know if there is anything we can arrange for' \
                                           'you before your arrival.' '\n' ' We wish you a pleasant travel ' \
                                           'to London and look forward to welcoming you.' '\n''\n' \
                                           'With warm regards,' '\n''\n' \
                                           'The staff of MyHotel.' \

        send_mail(
            'MyHotel - Booking confirmation',  # Subject
            final_body,
            settings.EMAIL_HOST_USER,   # From
            [email],  # To
            fail_silently=False,)

        return render(request, 'mainapp/booking_completed.html')

# Retrieve all the catogory of Extra
def retrieve_extra_category():
    extra = Extra.objects.all()      # Put all the objects in a model inside a variable
    list = []                        # Create an empty array
    for e in extra:                  # for {Some variables} execute the loop for {all the element in extra}
        if e.category not in list:   # Do not repeat the double element
            list.append(e.category)  # add to list all the Model.{Attributes you want}

    return list

# Retrieve all the types of extra
def retrieve_extra_types():
    extra_names = Extra.objects.all()  # Put all the objects in a model inside a variable
    list_type = []  # Create an empty array used for the names
    for e in extra_names:  # for {Some variables} execute the loop for {all the element in extra}
            list_type.append(e.extra_type)  # add to list all the Model.{Attributes you want}

    return list_type


# Retrieve all the types of extra
def retrieve_extra_prices():
    extra_prices = Extra.objects.all()  # Put all the objects in a model inside a variable
    list_price = []  # Create an empty array used for the prices
    for e in extra_prices:  # for {Some variables} execute the loop for {all the element in extra}
            list_price.append(e.price_night) # add to list all the Model.{Attributes you want}

    return list_price


# Retrieve all the types of room
def retrieve_room_types():
    rooms = RoomType.objects.all()  # Retrieve all the rooms
    return rooms


def homepage(request):
    room_type = retrieve_room_types()  # Retrieve all the rooms
    today = datetime.date.today()  # Retrieve today day
    addition_day = datetime.timedelta(days=1)  # add to any date 1
    day_after = datetime.date.today() + addition_day  # the day after today
    today_format = today.strftime('%d/%m/%y')  # today in the correct format
    day_after_format = day_after.strftime('%d/%m/%y') # tomorrow in the correct format
    nights = day_after - today  # calculate the nights

    dict = {
        'rooms': room_type,
        'tday' : today_format,
        'day_after': day_after_format,
        'nights': nights,

    }

    return render(request, 'mainapp/homepage.html', context=dict)


def about(request):

    return render(request, 'mainapp/about.html')


# This function send and email from the contact form.
def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']
        final_body = 'Guest name: ' + name + '\n''Guest email: ' + email + '\n''\n''Guest enquire: ''\n' + message

        send_mail(
            subject,  # Subject
            final_body,  # Message
            settings.EMAIL_HOST_USER,   # From
            [settings.EMAIL_HOST_USER],  # To
            fail_silently=False,)

    return render(request, 'mainapp/contact.html')


# This function makes the final reservation.
def reservation(request):

    # This variables all store the information from models.
    room_type = retrieve_room_types()
    extra_category = retrieve_extra_category()
    extra_names = retrieve_extra_types()
    extra_prices = retrieve_extra_prices()

    # This variables are used for the dates.
    addition_day = datetime.timedelta(days=1)  # add to any date 1
    check_in = datetime.date.today().strftime('%d/%m/%Y')
    day_after = datetime.date.today() + addition_day  # the day after today
    check_out = day_after.strftime('%d/%m/%Y')  # the day after today

    room_size = 'Select a room'
    number_room = 'Numb of room '

    if request.method == 'POST':
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        room_size = request.POST['room_size']
        number_room = request.POST['number_room']

        check_in_date = datetime.datetime.strptime(check_in, '%d/%m/%Y')
        check_out_date = datetime.datetime.strptime(check_out, '%d/%m/%Y')
        nights = (check_out_date - check_in_date).days

        request.session['nights'] = nights


    dict = {
            'extra' : extra_category,
            'rooms': room_type,
            'extra_names': extra_names,
            'extra_prices' : extra_prices,
            'check_in': check_in,
            'check_out': check_out,
            'room_size': room_size,
            'number_room': number_room,


    }
    return render(request, 'mainapp/reservation.html', context=dict)


def email_confirmed(request):
    return render(request, 'mainapp/email_confirmed.html')


def services(request):
    return render(request, 'mainapp/services.html')


def room_single(request):
    return render(request, 'mainapp/room_single.html')


def room_double(request):
    return render(request, 'mainapp/room_double.html')


def room_twin(request):
    return render(request, 'mainapp/room_twin.html')


def booking_confirm(request):

    check_in = request.POST['check_in']
    check_out = request.POST['check_out']
    room_size = request.POST['room_size']
    number_room = request.POST['number_room']


    dict = {
        'check_in': check_in,
        'check_out': check_out,
        'room_size': room_size,
        'number_room': number_room,

    }


    return render(request, 'mainapp/booking_confirm.html', context= dict)


def filter_room_prices(request):
    any = request.POST.get('any')
    room = RoomType.objects.all()
    room_type = room.filter(type=any)
    price_night = []
    for e in room_type:  # for {Some variables} execute the loop for {all the element in extra}

        price_night.append(e.price)  # add to list all the Model.{Attributes you want}
    price_night = json.dumps(price_night)

    days_total = 1
    nights = request.session.get('nights')  # Get the nights variable from another view
    request.session['nights'] = nights
    days_total = json.dumps(nights)



    number_rooms = request.POST.get('number_rooms')
    numb_rooms = json.dumps(number_rooms)

    addition_day = datetime.timedelta(days=1)  # add to any date 1
    day_after = datetime.date.today() + addition_day  # the day after today


    check_in2 = request.POST.get('check_in', default=datetime.date.today().strftime('%d/%m/%Y'))
    check_out = request.POST.get('check_out', default=day_after.strftime('%d/%m/%Y'))
    check_in2 = datetime.datetime.strptime(check_in2, '%d/%m/%Y')
    check_out = datetime.datetime.strptime(check_out, '%d/%m/%Y')
    nights = (check_out - check_in2).days



    dict = {
        'price_night': price_night,
        'day_total': days_total,
        'numb_rooms': numb_rooms,
        'nights': nights


    }
    return JsonResponse(dict, safe=False)


def filter(request):
    extra = Extra.objects.all()

    extra_names_t = extra.filter(category=1)
    list_type_t = []
    list_price_t = []
    for e in extra_names_t:  # for {Some variables} execute the loop for {all the element in extra}
            list_type_t.append(e.extra_type)  # add to list all the Model.{Attributes you want}
            list_price_t.append(e.price_night)  # add to list all the Model.{Attributes you want}

    extra_names_c = extra.filter(category=2)
    list_type_c = []
    list_price_c = []
    for e in extra_names_c:  # for {Some variables} execute the loop for {all the element in extra}
        list_type_c.append(e.extra_type)  # add to list all the Model.{Attributes you want}
        list_price_c.append(e.price_night)  # add to list all the Model.{Attributes you want}

    extra_names_b = extra.filter(category=3)
    list_type_b = []
    list_price_b = []
    for e in extra_names_b:  # for {Some variables} execute the loop for {all the element in extra}
        list_type_b.append(e.extra_type)  # add to list all the Model.{Attributes you want}
        list_price_b.append(e.price_night)  # add to list all the Model.{Attributes you want}

    extra_names_f = extra.filter(category=4)
    list_type_f = []
    list_price_f = []
    for e in extra_names_f:  # for {Some variables} execute the loop for {all the element in extra}
        list_type_f.append(e.extra_type)  # add to list all the Model.{Attributes you want}
        list_price_f.append(e.price_night)  # add to list all the Model.{Attributes you want}

    print(list_type_t)



    dict = {
        'list_price_t' : list_price_t,
        'list_type_t' : list_type_t,
        'list_price_c': list_price_c,
        'list_type_c': list_type_c,
        'list_price_b': list_price_b,
        'list_type_b': list_type_b,
        'list_price_f': list_price_f,
        'list_type_f': list_type_f,

    }


    return JsonResponse(dict, safe=False)


