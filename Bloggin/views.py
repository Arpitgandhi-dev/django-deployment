from django.shortcuts import render
from Bloggin.forms import UserForm, UserBlogData, Bloggindata

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def first(request):
    return render(request, 'Bloggin/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registrated = False

    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        profile_form = UserBlogData(data=request.POST)
        

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()



            registrated = True

        else:
            print(user_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserBlogData()
    return render(request, 'Bloggin/registration.html',
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registrated})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'Bloggin/login.html', {})
@login_required
def Bloggerfunc(request):

    blog_data = Bloggindata(data=request.POST)
    if request.method == 'POST':
        
        
        if blog_data.is_valid():
            blog_data.save()
            return HttpResponse('Bloggin/Blog.html')
    return render(request, 'Bloggin/Blog.html', {'blog_data': blog_data})
