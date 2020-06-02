from uuid import uuid4
from django.db import models

GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    key = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Zone(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Tour(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    operator = models.CharField(max_length=50, null=True, blank=True)
    tour_type = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    img = models.URLField()
    country = models.CharField(max_length=50, null=True, blank=True)
    takeoff_zone = models.ForeignKey(
        Zone,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tours_takeoff'
    )
    arrival_zone = models.ForeignKey(
        Zone,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tours_arrival'
    )

    def __str__(self):
        return f'{self.name}'