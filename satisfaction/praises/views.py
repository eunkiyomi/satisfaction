from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from datetime import datetime

from .models import Praise

# Create your views here.
def index(request, date_text=timezone.localtime().strftime("%Y%m%d")):
    latest_praise_list = Praise.objects.order_by('-pub_date')[:5]

    date = datetime.strptime(str(date_text), "%Y%m%d").date()
    praise_list = Praise.objects.filter(pub_date__date=date)

    context = {
        'latest_praise_list': latest_praise_list,
        'praise_list': praise_list,
        'date': date.strftime("%Y.%m.%d")
    }

    return render(request, 'praises/index.html', context)

def detail(request, praise_id):
    return HttpResponse("Bless you for what you do: %s" % praise_id)

def new(request):
    praise_text = request.POST['praise_text']
    date_text = request.POST['date_text']
    date = datetime.strptime(str(date_text), "%Y.%m.%d")

    p = Praise(praise_text=praise_text, pub_date=date)
    p.save()

    return HttpResponseRedirect(reverse("praises:index",
                                kwargs={'date_text': date.strftime("%Y%m%d")}))


def delete(request, praise_id):
    p = get_object_or_404(Praise, pk=praise_id)
    date = timezone.localtime(p.pub_date)
    p.delete()
    return HttpResponseRedirect(reverse("praises:index",
                                kwargs={'date_text': date.strftime("%Y%m%d")}))
