from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.forms.models import model_to_dict

from datetime import datetime
from operator import itemgetter

from .models import Praise, Profile, Photo
from .forms import PhotoForm
from django.contrib.auth.models import User

import re


# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse("praises:date",
                                kwargs={'date_text': datetime.now().strftime("%Y%m%d")}))

def date_view(request, date_text=datetime.now().strftime("%Y%m%d")):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("praises:login"))

    if request.user.profile.nickname == '':
        # return HttpResponse("you have to set your id first")
        return HttpResponseRedirect(reverse("praises:change_id"))

    user_praises = Praise.objects.filter(author=request.user)

    date = datetime.strptime(date_text, "%Y%m%d").date()
    praise_list = user_praises.filter(pub_date__date=date)

    recorded_dates = list(set(map(lambda p: p.pub_date.strftime("%Y%m%d"), user_praises)))

    photoURL = ''
    photo_exists = False

    photo = Photo.objects.filter(author=request.user).filter(pub_date__date=date)
    photo_exists = photo.exists()
    if photo_exists:
        photo = photo.last()

    context = {
        'photo_exists': photo_exists,
        'photo': photo,
        'recored_dates': recorded_dates,
        'praise_list': praise_list,
        'date': date.strftime("%Y.%m.%d"),
        'date_in_url': date.strftime("%Y%m%d")
    }

    return render(request, 'praises/index.html', context)

def detail(request, praise_id):
    return HttpResponse("Bless you for what you do: %s" % praise_id)

def new(request):
    praise_text = request.POST['praise_text']
    date_text = request.POST['date_text']
    date = datetime.strptime(date_text, "%Y%m%d")

    p = Praise(praise_text=praise_text, pub_date=date, author=request.user)
    p.save()

    return HttpResponseRedirect(reverse("praises:date",
                                kwargs={'date_text': date_text}))


def delete(request, praise_id):
    p = get_object_or_404(Praise, pk=praise_id)
    date = p.pub_date

    if p.author == request.user:
        p.delete()

    return HttpResponseRedirect(reverse("praises:date",
                                kwargs={'date_text': date.strftime("%Y%m%d")}))

def login(request):
    return render(request, 'praises/login.html')

def change_id(request):
    return render(request, 'praises/change_id.html')

def set_id(request):
    new_nickname = request.POST['id_text']

    if len(new_nickname) > 30:
        return render_message(request, "Too long! Please use other id...:O")

    if Profile.objects.filter(nickname=new_nickname).exists():
        return render_message(request, "It already exists! please use other id.")
    else:
        request.user.profile.nickname = new_nickname
        request.user.save()
        # return HttpResponse("We just change your id to" + new_nickname)

    return HttpResponseRedirect(reverse("praises:index"))

def set_photo(request, date_text):
    date = datetime.strptime(date_text, "%Y%m%d")

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.pub_date = date
            photo.author = request.user
            photo.save()

            return HttpResponseRedirect(reverse("praises:date", kwargs={'date_text': date_text}))

    photo = Photo.objects.filter(author=request.user).filter(pub_date__date=date)
    photo_exists = photo.exists()
    if photo_exists:
        photo = photo.last()

    context = {
        'photo_exists': photo_exists,
        'photo': photo,
        'date': date_text,
        'form': PhotoForm()
    }
    return render(request, 'praises/upload_photo.html', context)

def backup(request):
    praises = Praise.objects.filter(author=request.user)
    backup_list = list(praises.values('pub_date', 'praise_text'))
    backup_list.sort(key=itemgetter('pub_date'))

    str = ""
    date = datetime(1980, 1, 1, 0, 0)
    for praise in backup_list:
        if praise['pub_date'] != date:
            str += "## " + praise['pub_date'].strftime("%Y%m%d") + "\n"
            date = praise['pub_date']

        str += "- " + praise['praise_text'] + "\n"

    return render(request, 'praises/backup.html', {"text": str})

def settings(request):
    return render(request, 'praises/settings.html')

def render_message(request, msg):
    return render(request, 'praises/message.html', {"msg": msg})
