from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# 데이터가 보여지는 모습

class User(AbstractUser):
    # AbstractUser를 상속한 User 클래스
