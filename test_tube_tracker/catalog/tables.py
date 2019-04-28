import django_tables2 as tables
from .models import Sample
from django_tables2.utils import A  # alias for Accessor

class SampleTable(tables.Table):
    Name = tables.LinkColumn('sample-detail', args=[A('pk')])
    
    class Meta:
        model = Sample
        exclude = ('id', 'Description', 'Owner', 'Date' )
        template_name = 'django_tables2/bootstrap4.html'

    
        