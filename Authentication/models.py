from django.db import models

class Records(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=13)
    Address=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=6)

    def __str__(self):
        return self.first_name
