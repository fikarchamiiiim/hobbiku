from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_pic = models.ImageField(upload_to='menu/img/',blank=True)

    def __str__(self):
        return self.category_name

class Menu(models.Model):
    judulMenu = models.CharField(max_length=225)
    descMenu = models.TextField()
    picMenu = models.ImageField(upload_to='menu/img/',blank=True)
    posterMenu = models.ImageField(upload_to='menu/img/', blank=True)
    hargaMenu = models.IntegerField(default=0)
    diskon = models.IntegerField(default=0)
    kuantitas = models.IntegerField(default =  0)
    slug = models.SlugField(default='product-', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.judulMenu)

    class Meta:
        unique_together = ('judulMenu','slug')

    def get_price(self):
        return self.hargaMenu
    
    def get_absolute_url(self):
        return reverse("menu:produkSatuan", kwargs={"Slug":self.Slug})

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #addtional
    alamat = models.TextField(max_length=128)
    Provinsi = models.CharField(max_length=64)
    Kota = models.CharField(max_length=64)
    Kecamatan = models.CharField(max_length=64)
    Kelurahan = models.CharField(max_length=64)
    profile_pic = models.ImageField(upload_to ='profile/profile_pics', blank=True)
    

    def __str__(self):
        return self.user.username

class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)
    
    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')

VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package'),
)

class Variation(models.Model):
    product = models.ForeignKey('Menu', on_delete=models.CASCADE)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    title = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.title


