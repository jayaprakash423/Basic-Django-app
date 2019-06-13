from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .forms import MusicianForm,AlbumForm
from .models import Musician,Album
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.

def index_view(request):
	musician=Musician.objects.all()

	context={"musician":musician}
	return render(request,'index.html',context)

def create_Musician_view(request):
	form=MusicianForm(request.POST or None)
	if form.is_valid():
		# firstname=form.clean_data['first_name']
		# lastname=form.clean_data['last_name']
		# album=form.clean_data['album']
		form.save()
		messages.success(request,'user enter successfully')
	context={'form':form}
	
	return render(request,'create.html',context)

def create_Album_view(request):
	form1=AlbumForm(request.POST or None)
	if form1.is_valid():
		form1.save()
		messages.success(request,'album created successfully')
	context={'form1':form1}
	
	return render(request,'create1.html',context)

def about_view(request):
	title="All about the networks"
	cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '17,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},

    {'name': 'Mumbai', 'population': '12,000,000', 'country': 'Austrlia'},
    {'name': 'Calcutta', 'population': '55,000,000', 'country': 'Southafrica'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '5,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '22,000,000', 'country': 'London'},

    {'name': 'Mumbai', 'population': '29,000,000', 'country': 'England'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'Newzland'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '17,000,000', 'country': 'UK'},
    {'name': 'Tokyo', 'population': '13,000,000', 'country': 'UAE'},

    {'name': 'Mumbai', 'population': '10,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '25,000,000', 'country': 'WestIndies'},
    {'name': 'New York', 'population': '10,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '36,000,000', 'country': 'Srilanka'},
    {'name': 'Tokyo', 'population': '13,000,000', 'country': 'Japan'},

    {'name': 'Mumbai', 'population': '96,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '30,000,000', 'country': 'Chaina'},
    {'name': 'New York', 'population': '50,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '5,000,000', 'country': 'Singapore'},
    {'name': 'Tokyo', 'population': '3,000,000', 'country': 'UAE'},
]
	context={"title":title,"cities":cities}
	return render(request,'about.html',context)

def update_view(request,id=1):
	blog_get=get_object_or_404(Musician,id=id)
	if request.method=="POST":
		form=MusicianForm(request.POST,instance=blog_get)
		try:
			if form.is_valid():
				form.save()
				messages.success(request,"your data is updated successfully")

		except Exception as e:
			messages.warning(request,"your entered data is incorrect {}".format(e))

	else:
		form=MusicianForm(instance=blog_get)
	context={
	     'form':form,
	     'blog_get':blog_get
	  }
	return render(request,'update.html',context)



def delete_view(request):
	title="hello delete"
	context={"title":title}
	return render(request,'delete.html',context)

def contact_view(request):
	title="hello contact"
	context={"title":title}
	return render(request,'contact.html',context)

def retrive_view(request):
	album=Album.objects.all()
	context={"album":album}
	return render(request,'retrive.html',context)
	

		
	
	



def login_view(request):
	
	return render(request,'login.html',context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'blogs/register.html', {'form': form})


