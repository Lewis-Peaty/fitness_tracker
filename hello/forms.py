from django import forms, utils
from django.db import models
from django.forms import ModelForm
from .models import Workout

WORKOUT_CHOICES = (
    ('Arms','Custom','Legs','Shoulders','Core','Back','BitsNBops','Cardio','Chest')                            
)

class WorkoutForm(ModelForm):

    class Meta:
        model = Workout
        fields = ['name', 'workout', 'n_exercises', 'avg_sets']

