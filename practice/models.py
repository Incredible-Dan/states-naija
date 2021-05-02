from django.db import models


# Create your models here.
class State(models.Model):
    state_text = models.CharField(max_length=50)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return self.state_text


class Capital(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    capital_text = models.CharField(max_length=50)
    # tribe = models.CharField(max_length=40)

    def __str__(self):
        return self.capital_text


class Region(models.Model):
    region = models.ForeignKey(State, on_delete=models.CASCADE)
    region_text = models.CharField(max_length=50)

    def __str__(self):
        return self.region_text


class Tribe(models.Model):
    tribe = models.ForeignKey(State, on_delete=models.CASCADE)
    tribe_text = models.CharField(max_length=50)

    def __str__(self):
        return self.tribe_text
