from django.db import models
# Create your models here.

class FormData(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
    ]

    MATERIALS_PROVIDE = [
        ('credit_card', 'Credit_card'),
        ('debit_card', 'Debit_card'),
        ('checkbook', 'Checkbook'),
    ]


    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=100)
    mail_id = models.EmailField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100, choices=ACCOUNT_TYPE_CHOICES)
    materials_provide = models.CharField(max_length=100,choices=MATERIALS_PROVIDE)


    def __str__(self):
        return self.name
