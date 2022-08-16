

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize

from blog.models import Comment
from users.models import Profile



from . forms import LoginUser, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            fisrt_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            def _user_full_name(**kwags):
                #fullname = fisrt_name + ' ' + last_name
                return f'{fisrt_name} {last_name}'.capitalize
            form.save()

            messages.success(request, f'Account created successfully for {_user_full_name()} and you account id is {username}')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def login_user(request):
    form = LoginUser()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
            userexisth = True
        except:
            userexisth = False
            return messages.error(request, 'User does not existh')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            profile = Profile.objects.get(user=user)
            serialize('json', profile, cls=LazyEncoder)
            request.session['profile'] = profile
            return redirect('blog-home')
    
        elif not userexisth:
            return messages.error(request, 'Password does not match')

    context = {
        'form':form
    }
    return render(request, 'users/login.html', context)
    
@login_required(login_url='login')
def profile(request, pk):

    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You successfully updated your profile')
            return redirect('profile', pk=profile.pk)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    fullname =  request.user.get_full_name()

    context = {
        'fullname': fullname,
        'u_form':u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)


# class PostComment(CreateView):
#     model = CommentOnPost
#     fields = ['comment_text']
#     template_name = 'user/comment.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)#, redirect('blog-home')

