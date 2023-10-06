from django.db import models

# Create your models
class RegisterFormModel(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    class Meta:
        ordering=['username']
    def __str__(self):
        return '{}'.format(self.username)