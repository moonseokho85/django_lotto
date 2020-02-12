from django.shortcuts import render, redirect
from django.http import HttpResponse # 추가됨
from lotto.models import GuessNumbers
from lotto.forms import PostForm
# Create your views here.

def index(request):
    '''
    site_1\lotto\templates\default.html (X) -> site_1\lotto\templates\lotto\default.html (O)

    site_1\member\templates\index.html (127.0.0.1:8000/member/)
    site_1\products\templates\index.html (127.0.0.1:8000/products)
    site_1\history\templates\index.html (127.0.0.1:8000/history)

    templates\index.html, index.html, index.html (X)

    site_1\member\templates\member\index.html (127.0.0.1:8000/member/)
    site_1\products\templates\products\index.html (127.0.0.1:8000/products)
    site_1\history\templates\history\index.html (127.0.0.1:8000/history)

    templates\ member\index.html, products\index.html, history\index.html (O)
    '''
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos': lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

from .forms import PostForm
def post(request):
    print("********")
    print(request.method)
    print("********")
    print(request.POST)
    print("********")

    # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
    if request.method == "POST": # filled form
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False) # DB 저장은 아래 generate 함수의 . 로 처리
            lotto.generate()
            return redirect('index') # urls.py 의 name='index' 에 해당

    else:
        form = PostForm() # empty form
        return render(request, 'lotto/form.html', {"form": form})

    form = PostForm()
    return render(request, "lotto/form.html", {"form": form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})
