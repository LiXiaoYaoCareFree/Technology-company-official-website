from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide
from team.models import Team

# Create your views here.
def index(request):
    # 获取slide表中的所有数据
    slides = Slide.objects.all()
    # 获取team表中的所有数据
    teams = Team.objects.all().order_by('rank')
    return render(request, 'index.html', {
        'slides': slides,
        'team': teams,
        })


