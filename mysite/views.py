from django.http import HttpResponse
from django.shortcuts import render
from news.models import News
from slide.models import Slide
from team.models import Team

# Create your views here.
def index(request):
    # 获取slide表中的所有数据
    slides = Slide.objects.all()
    # 获取team表中的所有数据
    teams = Team.objects.all().order_by('rank')
    # 获取news表中的所有数据
    news = News.objects.filter(category_id=1).order_by('-created_at')[:3]
    # 获取成功案例
    cases = News.objects.filter().exclude(category_id=1).order_by('-created_at')[:6]
    return render(request, 'index.html', {
        'slides': slides,
        'team': teams,
        'news': news,
        'cases': cases,
        })


