from django.db import models
from django.conf import settings
import os
from django.contrib import admin
from django.utils.safestring import mark_safe


# Create your models here.
class TeaStallProducts(models.Model):
    class Meta:
        verbose_name = "Tea Shop"

    # item_id=models.IntegerField()
    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    item_price = models.FloatField()
    # item_image=models.ImageField(upload_to="static", null=True, blank=True)
    item_image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)

    def url(self):
        return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.item_image)))

    def price_value(self):
        if self.item_price:
            return 'INR {}'.format(self.item_price)

    def image_tag(self):
        if self.item_image:
            return mark_safe('<img src="%s" style="width: 95px; height:55px;" />' % self.url())
        else:
            return 'No Image Found'

    def __str__(self):
        return 'Name:{0} ,Price:INR{1},Description:{2},Image:{3}'.format(self.item_name, self.item_price,
                                                                         self.item_description, self.item_image)
