from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone

# Create your models here.
class Bookmark (models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    pub_date = models.DateTimeField('date_published')
    memo = models.CharField(max_length=200)

    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    def __str__ (self):
        return "이름: "+self.site_name +"주소: " +self.url
    def get_absolute_url (self):
        return reverse('detail', args=[str(self.id)])