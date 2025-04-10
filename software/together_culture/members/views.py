from django.shortcuts import render, redirect
from .models import Member, Event, Visit
from .forms import MemberForm

def search_members(request):
    query = request.GET.get('q')
    if query:
        members = Member.objects.filter(name__icontains=query)
        non_members = Visit.objects.filter(member__isnull=True, event__name__icontains=query)
    else:
        members = Member.objects.none()
        non_members = Visit.objects.none()
    visits = Visit.objects.filter(member__in=members)
    return render(request, 'members/search_members.html', {'members': members, 'non_members': non_members, 'visits': visits})

def search_events(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter(name__icontains=query)
    else:
        events = Event.objects.none()
    visits = Visit.objects.filter(event__in=events)
    return render(request, 'members/search_events.html', {'events': events, 'visits': visits})

def home(request):
    return render(request, 'members/home.html')

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})
