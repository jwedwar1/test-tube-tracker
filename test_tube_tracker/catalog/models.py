from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Sample(models.Model):
    Name = models.CharField(max_length = 50, default = '', help_text='Enter the name of the sample')
    Date = models.DateField(null=True, blank=True)
    Location = models.CharField(max_length = 20, default = '', help_text='Enter the index of the sample in the freezer')
    Description = models.CharField(max_length=500, blank=True, default='', help_text='Optional: enter a brief description of the sample')
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    OwnerFullName = models.CharField(max_length = 50, default = '')


    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('sample-detail', args=[str(self.pk)])
