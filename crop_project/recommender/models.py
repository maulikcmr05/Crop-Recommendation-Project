from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,reversed_name='predictions')
    crop_name = models.CharField(max_length=100)
    predicted_yield = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.crop_name} - {self.predicted_yield}"