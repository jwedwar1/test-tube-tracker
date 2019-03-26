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
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.http import HttpResponse

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



def AddSample(request):
    if request.method == 'POST':
        form = SampleAddForm(request.POST)
        if form.is_valid():
            Sample = form.save(commit=False)
            Sample.Owner = request.user
            Sample.OwnerFullName = request.user.first_name + " " + request.user.last_name
            Sample = Sample.save()
            return redirect('sample_list')
    else:
        form = SampleAddForm()
    return render(request, 'add_sample2.html', {'form': form})




class SampleListView(generic.ListView):
    model = Sample

class SampleDetailView(generic.DetailView):
    model = Sample

class SampleUpdate(UpdateView):
    model = Sample
    fields = ['Name', 'Date', 'Location', 'Description']

class SampleDelete(DeleteView):
    model = Sample
    success_url = reverse_lazy('sample_list')





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

            return render(request, 'catalog/search_results.html', {'samples': samples, 'query': q})
    return render(request, 'catalog/search_form.html', {'error': error})