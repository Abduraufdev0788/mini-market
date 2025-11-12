from django.db import models

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Oziq-ovqat'),
        ('drinks', 'Ichimliklar'),
        ('clothes', 'Kiyim-kechak'),
        ('electronics', 'Elektronika'),
        ('appliances', 'Maishiy texnika'),
        ('accessories', 'Aksessuarlar'),
        ('kids', 'Bolalar uchun mahsulotlar'),
    ]
    name = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.FloatField()
    viewers = 0
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY_CHOICES)
    discount = models.IntegerField()

    def __str__(self):
        return f"{self.name}  {self.price}"


