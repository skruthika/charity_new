from django.shortcuts import render,redirect
from .forms import SignupForm
from django.http import HttpResponse
from django.template import loader
def index1(request):
    return render(request,"home1.html")
def index2(request):
    return render(request,"home2.html")
def index3(request):
    tem=loader.get_template("signin.html")
    return HttpResponse(tem.render())


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('index3')  # Replace with the appropriate URL name
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
def index5(request):
    tem=loader.get_template("thank.html")
    return HttpResponse(tem.render())
def index6(request):
    tem=loader.get_template("about.html")
    return HttpResponse(tem.render())
  