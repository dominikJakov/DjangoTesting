from django.shortcuts import render
from .models import Event
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import EventForm


def say_hello(request):
    #return HttpResponse("<h1> Welcome to my store </h1>")
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    event_list = Event.objects.all()
    form = EventForm
    return render(request, 'hello.html',{ 'event_list' : event_list, 'form' : form})
    #return render(request,'hello.html', { 'name' : 'BEzos'})

def all_events(request):
    all_events_list = Event.objects.all()
    return render(request, 'hello.html')

def results(request):
    inp_value = request.GET.get('results', 'This is a default value')
    context = {'inp_value': inp_value}
    return render( request, 'results.html', context)