from django.db import models

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    img = models.TextField(max_length=450)

     # new code below
    def __str__(self):
        return self.name

#Feeding model
class Feeding(models.Model):
    # the first optional positional argument overrides the label
    date = models.DateField('feeding date')
    
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
    # Create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
    
     # change the default sort
    class Meta:
     ordering = ['-date']


