from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from tools.shortcuts import render,redirect

from forms import *
from models import *
def activity_create(request,template='activity_form.html'):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit = False)
            activity.creator = User.objects.get(pk=1)#request.user
            activity.save()
            return redirect(request, activity)
    else:
        form = ActivityForm()
    return render(request,template,{'form':form})

def activity_list(request,template='activity_list.html'):
    activity_list = Activity.objects.all()
    return render(request,template,{'activity_list':activity_list})

def activity_detail(request,slug,template='activity_detail.html'):
    activity = get_object_or_404(Activity,slug=slug)
    return render(request,template,{'activity':activity})
