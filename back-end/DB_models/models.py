from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, age, password=None, **extra_fields):
        if not email:
            raise ValueError('Користувач повинен мати email')
        email = self.normalize_email(email)
        if not first_name or not last_name:
            raise ValueError("Ім'я та прізвище обов'язкові")

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
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_seller = models.BooleanField(default=False)

    user_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions", blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating and not self.user_id:
            self.user_id = f"{self.first_name.lower()}_{self.last_name.lower()}_{self.pk}"
            super().save(update_fields=["user_id"])

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.user_id})"


class Talent_dsc(models.Model):
    prof = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.prof


class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    talent_dsc = models.ForeignKey(Talent_dsc, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.position} ({self.talent_dsc.prof})"


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)  # замість user_id
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.project.title} — {self.talent.position} — ${self.price}"
