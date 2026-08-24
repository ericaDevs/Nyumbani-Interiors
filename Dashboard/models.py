from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 200, blank = False)
    email = models.EmailField(max_length = 200, null = False, unique = True)
    password = models.CharField(max_length = 8, blank = False)

    def __str__(self):
        return self.password