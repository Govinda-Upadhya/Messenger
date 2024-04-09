from django.shortcuts import render

# Create your views here.
def home(request):
    
    if request.user.is_authenticated:
        user=request.user
        return render(request,"home.html",{
            'user':user
        })
    return render(request,"home.html",{
            'user':None
        })
