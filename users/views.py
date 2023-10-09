from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home.html')



def logout_page(request):
    logout(request)
    return redirect('home')