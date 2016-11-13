from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import Workout, Food
from datetime import datetime

from .models import Greeting
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import WorkoutForm, FoodForm
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


#WORKOUTS!
def get_all_workouts(request):
    workouts = Workout.objects.all()
    template = loader.get_template('get_all_workouts.html')
    context = {
        'workouts' : workouts,
    }
    return HttpResponse(template.render(context,request))

def add_workout(request):
   # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkoutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/get_all_workouts')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkoutForm()

    return render(request, 'new_workout.html', {'form': form})
    
def remove_workout(request):
    Workout.objects.latest('time_stamp').delete()
    return HttpResponseRedirect('/get_all_workouts')
        
        
        
#FOOD!
def get_all_food(request):
    foods = Food.objects.all()
    template = loader.get_template('get_all_food.html')
    context = {
        'foods' : foods,
    }
    return HttpResponse(template.render(context,request))

def add_food(request):
   # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/get_all_food')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FoodForm()

    return render(request, 'new_food.html', {'form': form})
        
def remove_food(request):
    Food.objects.latest('time_stamp').delete()
    return HttpResponseRedirect('/get_all_food')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
