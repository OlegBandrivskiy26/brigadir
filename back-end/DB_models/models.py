from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, age, password=None, **extra_fields):
        if not email:
            raise ValueError('Користувач повинен мати email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if not first_name or not last_name:
            raise ValueError("Ім'я та прізвище обов'язкові")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            age=age,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, age, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, age, password, **extra_fields)

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_seller = models.BooleanField(default=False)

    user_id = models.CharField(max_length=100, unique=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions", blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.user_id:
            super().save(*args, **kwargs)  # Перше збереження для створення `pk`
            self.user_id = f"{self.first_name.lower()}_{self.last_name.lower()}_{self.pk}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_id


class Talent_dsc(models.Model):
    prof = models.CharField(max_length=100)

class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    talent_dsc = models.ForeignKey(Talent_dsc, on_delete=models.PROTECT)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Contract(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    talent_id = models.OneToOneField(Talent, on_delete=models.CASCADE)
    project_id = models.OneToOneField(Project, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)









