from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=50, choices=[
        ('New Equipment Request', 'New Equipment Request'),
        ('Replacement Request', 'Replacement Request')
    ])

class Theatre(models.Model):
    number = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    rvp = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} - {self.name}"


class Equipment(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    # serial_number = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_number = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="equipment_photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.item_number}"


class Request(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    #requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    request_date = models.DateField(auto_now_add=True)
    approval_status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected')
        ],
        default='Pending'  # ✅ sets default value
    )
    requisition_number = models.CharField(max_length=50, blank=True, null=True)
    po_number = models.CharField(max_length=50, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    business_case = models.TextField(default="Not provided")
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='requester_user')


    
    @property
    def total_price(self):
        return self.equipment.price + self.shipping_cost + self.tax

    def __str__(self):
        return f"Request #{self.id} - {self.equipment} for {self.theatre}"



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.theatre.name if self.theatre else 'No Theatre'}"

