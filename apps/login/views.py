from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'login/index.html')
def process(request):
    if request.method == 'POST':
        if request.POST['button']==Register:
            return redirect(reverse('home:home'))
        else:
            return redirect(reverse('home:home'))
    return redirect(reverse('login:login'))
