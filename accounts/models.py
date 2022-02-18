from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # Could inherit from AbstractBaseUser which is more flexible, but need more work
    pass



# Create your models here.
