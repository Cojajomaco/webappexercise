from django.db import models
# Choice constraints for various model data
size_choices = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)

# Our 1-5 rating scale
int_choices = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


# Create your models here.

# Dog class. For dogs. It's dogs. And things about dogs.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# These are dog breeds. For dogs. Again.
class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100, choices=size_choices)
    friendliness = models.IntegerField(choices=int_choices)
    trainability = models.IntegerField(choices=int_choices)
    sheddingamount = models.IntegerField(choices=int_choices)
    exerciseneeds = models.IntegerField(choices=int_choices)

    def __str__(self):
        return self.name