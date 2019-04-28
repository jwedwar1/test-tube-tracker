from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, CreateSampleForm, SampleAddForm
from django.views import generic
from .models import Sample
from .tables import SampleTable
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import django_tables2 as tables
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2 import A
from django_tables2 import RequestConfig


from django.http import HttpResponse



def class_view_decorator(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.

    Can't subclass the `View` as it breaks inheritance (super in particular),
    so we monkey-patch instead.
    """

    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return simple_decorator



def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




class CreateSampleView(generic.CreateView):
    form_class = CreateSampleForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


@login_required
def AddSample(request):
    if request.method == 'POST':
        form = SampleAddForm(request.POST)
        if form.is_valid():
            Sample = form.save(commit=False)
            Sample.Owner = request.user
            Sample.OwnerFullName = request.user.first_name + " " + request.user.last_name
            Sample.Location = str(Sample.Shelf) + "" + str(Sample.Row) + "" + str(Sample.Column) + "" + str(Sample.Box) + "" + str(Sample.BoxRow) + "" + str(Sample.BoxColumn)
            Sample.DateString = str(Sample.Date)
            Sample = Sample.save()
            return redirect('home')
    else:
        form = SampleAddForm()
    return render(request, 'add_sample2.html', {'form': form})
    #return redirect('home')




class SampleListView(generic.ListView):
    model = Sample
    paginate_by = 10
    

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'Description')
        # validate ordering here
        return ordering

class SampleDetailView(generic.DetailView):
    model = Sample

@class_view_decorator(login_required)
class SampleUpdate(UpdateView):
    model = Sample
    fields = ['Name', 'DateString', 'Location', 'Description', 'Shelf', 'Row', 'Column', 'BoxRow', 'BoxColumn']

@class_view_decorator(login_required)
class SampleDelete(DeleteView):
    model = Sample
    success_url = reverse_lazy('home')





def search_form(request):
    return render(request, 'catalog/search_form.html')



def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            
        else:
            samples = Sample.objects.filter(Name__icontains=q) or Sample.objects.filter(Date__icontains=q) or Sample.objects.filter(Location__icontains=q) or Sample.objects.filter(Description__icontains=q) or Sample.objects.filter(OwnerFullName__icontains=q)

            
            table = SampleTable(samples)
            RequestConfig(request, paginate={'per_page': 10}).configure(table)
            return render(request, 'searchtable.html', {'table': table})

            #return render(request, 'catalog/search_results.html', {'samples': samples, 'query': q})
    #return render(request, 'catalog/search_form.html', {'error': error})
    return render(request, 'searchtable.html', {'error': error})



class TableView(tables.SingleTableView):
    table_class = SampleTable
    queryset = Sample.objects.all()
    Name = tables.LinkColumn('sample_detail', args=[A('pk')])
    template_name = "simple_list.html"
    paginate_by = 10
    
    
    def get_table_kwargs(self):
        return {
            'exclude': ('Description', 'Owner', 'id', )
        }


#class TableView(SingleTableMixin, FilterView):
 #   table_class = SampleTable
 #   model = Sample
  #  template_name = 'simple_list.html'

 #   filterset_class = Sample.Date


def sampledef(request):
    table = SampleTable(Sample.objects.all())
    #RequestConfig(request).configure(table)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'table.html', {'table': table})
    