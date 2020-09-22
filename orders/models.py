import os
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from cart.models import cart

User = get_user_model()

pilihanStatus = (
    ('Mulai','Mulai'),
    ('Ditolak','Ditolak'),
    ('Selesai','Selesai'),
)

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    order_id = models.CharField(max_length=120, default='test', unique=True)
    Cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, default='Mulai', choices=pilihanStatus)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    buktiPembayaran = models.FileField(upload_to = 'bukti_pembayaran/', blank=True, null=True)

    def __str__(self):
        return str("{}, {}, {}".format(self.timestamp, self.order_id,self.user))
        