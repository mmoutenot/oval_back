from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from oval.api import UserResource
from oval.forms import LoginForm

# def auth(request):
#     if request.method=='GET' and request.user.is_authenticated():
#         ur = UserResource()
#         ur_bundle = ur.build_bundle(obj=request.user, request=request)
#         return HttpResponse(ur.serialize(None, ur.full_dehydrate(ur_bundle), 'application/json'))
#     elif request.method=='POST' and request.POST['email'] and request.POST['password']:
#         user = authenticate(username=username, password=password)
#         return HttpResponse("AUTHED")
#     return HttpResponse("NOAUTH")

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return render_to_response('index.html')
    elif request.GET and request.user.is_authenticated():
        return render_to_response('index.html')
    return render_to_response('login.html')
