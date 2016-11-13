from django.db import models
from datetime import datetime

LEWIS = "Lewis Peaty"
NAME_CHOICES = (
    (LEWIS , "Lewis"),
)
    

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    
       
class Workout(models.Model):
    ARMS = "ARM"
    LEGS = "LEG"
    SHOULDERS = "SHL"
    CORE = "COR"
    BACK = "BCK"
    BITSNBOBS = "BNB"
    CUSTOM = "CUS"
    CARDIO = "CRD"
    CHEST = "CHT"
    
    
    WORKOUT_CHOICES = (
        (ARMS , "Arms"),
        (LEGS , "Legs"),
        (SHOULDERS , "Shoulders"),
        (CORE , "Core"),
        (BACK , "Back"),
        (BITSNBOBS , "BitsNBobs"),
        (CUSTOM , "Custom"),
        (CARDIO , "Cardio"),
        (CHEST , 'Chest'),
    )
    
    name = models.CharField('your name',choices = NAME_CHOICES, default=LEWIS, max_length = 30)
    time_stamp = models.DateTimeField('time stamp',default=datetime.now, blank=True)
    n_exercises = models.IntegerField('number of exercises performed',default=4)
    avg_sets = models.IntegerField('average sets per exericse',default=4)
    workout = models.CharField(
        max_length = 3,
        choices = WORKOUT_CHOICES,
        default=CUSTOM
    )
    @property
    def total_sets(self):
        return self.n_exercises * self.avg_sets
    # @classmethod
    # def create(cls,value):
    #     point = cls(value=value)
    #     return point
    
    
    
    
    
class Food(models.Model):
    FRUIT = "Fruit"
    COFFEE = "Coffee"
    SALAD = "Salad"
    PASTRY = "Pastry"
    RICE = "Rice"
    NOODLES = "Noodles"
    OTHER = "Other"
    BEER = "Beer"
    MEAT = "Meat"
    FISH = "Fish"
    BURG = "Sandwich/Burger"
    NUTS = "Nuts-TrailMix"
    DURIAN = "Durian Fruit Oh No"
    DESSERT = "Dessert"
    
    FOOD_CHOICES = (
        (FRUIT , "Fruit"),
        (COFFEE , "Coffee"),
        (SALAD , "Salad"),
        (PASTRY , "Pastry"),
        (RICE , "Rice"),
        (NOODLES , "Noodles"),
        (OTHER , "Other"),
        (BEER , "Beer"),
        (MEAT , "Meat"),
        (FISH , "Fish"),
        (BURG , "Sandwich/Burger"),
        (NUTS , "Nuts-TrailMix"),
        (DURIAN , "Durian Fruit Oh No"),
        (DESSERT , "Dessert"),
    )    
    
    
    name = models.CharField('your name',choices = NAME_CHOICES, default=LEWIS, max_length = 30)
    time_stamp = models.DateTimeField('time stamp',default=datetime.now, blank=True)
    quantity = models.DecimalField(decimal_places=1,max_digits=3,default=1)
    food = models.CharField(
        max_length = 30,
        choices = FOOD_CHOICES,
        default=COFFEE
    )
    
