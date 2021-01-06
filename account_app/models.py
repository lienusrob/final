
from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #orders = models.ManyToManyField(Order, blank=True)
    #addresses = models.ManyToManyField(Address)
    # items_ordered = models.ManyToManyField(OrderItem)
    def __str__(self):
        return f'{self.user.username}\'s Profile'

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=400)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AnonymousReview(models.Model): 
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=400)
    data_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 