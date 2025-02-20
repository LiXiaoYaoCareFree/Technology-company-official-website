from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide

# Create your views here.
def index(request):
    # 获取slide表中的所有数据
    slides = Slide.objects.all()
    return render(request, 'index.html', {'slides': slides})