from django.db import models
from django.core.exceptions import ValidationError

class signup(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Use CharField for password
    confirm_password = models.CharField(max_length=128)  # Confirm password field
    

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run validation before saving
        super(signup, self).save(*args, **kwargs)

class donation(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    category_choices = [
        (1, 'Education'),
        (2, 'Healthcare'),
        (3, 'Poverty Allivation'),
        (4, 'Environment'),
        (5, 'Others'),
    ]
    selectacause = models.IntegerField(choices=category_choices)# Confirm password field
    message = models.CharField(max_length=100)