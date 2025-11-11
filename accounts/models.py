from django.db import models

class Accounts(models.Model):
    ROLES = (
        ("seller", "Seller"),
        ("customer", "Customer"),
    )
    first_name = models.CharField( max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    pasword = models.CharField(max_length=256)
    pasword_test = models.CharField(max_length=256)
    rol = models.CharField(choices=ROLES)

    def __str__(self):
        return f"{self.id}. {self.first_name} - {self.last_name} -- {self.rol}"
