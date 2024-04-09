from django.shortcuts import render
from .forms import SignUpForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str 
from django.core.mail import EmailMessage 
from .token import account_activation_token
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def Login(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page after login
                return redirect("Home")
    return render(request,"login.html",{
        'forms':form
    })
def custom_logout(request):
    logout(request)
    return redirect("Home")
def signup(request):
    signup=SignUpForm
    if request.method=="POST":
        signup=SignUpForm(request.POST)
        if signup.is_valid():
            user=signup.save(commit=False)
            user.is_active=True
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link for messenger app'
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            }) 
            to_email = signup.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')
            
        

    return render(request,'signup.html',{
        'forms':signup
    })
def activate(request, uidb64, token):  
    
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect("login") 
    else:  
        return HttpResponse('Activation link is invalid!') 
