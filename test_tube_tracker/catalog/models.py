from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import datetime
import django_tables2 as tables
from django_tables2 import A

class Sample(models.Model):
    SHELFCHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    ROWCHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    COLUMNCHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    BOXCHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
    )
    BOXROWCHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    BOXCOLUMNCHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    Name = models.CharField(max_length = 50, default = '', help_text='Enter the name of the sample')
    Date = models.DateField(null=True, blank=True, default = datetime.date.today())
    Location = models.CharField(null=True, blank=True, max_length = 20, default = '', help_text='Enter the index of the sample in the freezer')
    Description = models.CharField(max_length=500, blank=True, default='', help_text='Optional: enter a brief description of the sample')
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    OwnerFullName = models.CharField(max_length = 50, default = '', verbose_name = "Owner Name")
    Shelf = models.IntegerField(null=True, choices=SHELFCHOICES)
    Row = models.IntegerField(null=True, choices=ROWCHOICES)
    Column = models.IntegerField(null=True, choices=COLUMNCHOICES)
    Box = models.IntegerField(null=True, choices=BOXCHOICES, help_text='Box 1 is closest to you, Box 3 is farthest')
    BoxRow = models.IntegerField(null=True, choices=BOXROWCHOICES)
    BoxColumn = models.IntegerField(null=True, choices=BOXCOLUMNCHOICES)


    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this sample."""
        return reverse('sample-detail', args=[str(self.pk)])





#class SampleTable(tables.Table):
#    class Meta:
 #       model = Sample
 #       template_name = 'django_tables2/bootstrap4.html'
        #sequence = ('Name', 'Date', 'Location', 'OwnerFullName')
 #       Name2 = tables.LinkColumn('sample_detail', args=[A('pk')])
        #template_name = 'C:\Users\James\Desktop\senior_project\test_tube_tracker\templates\catalog\templates\jamesbootstrap4.html'
