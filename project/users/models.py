from django.contrib.auth.models import AbstractUser


# prevent from future maintenance cost to customize the django built-in user model
class User(AbstractUser):
    pass
