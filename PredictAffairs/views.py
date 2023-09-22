from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PredictAffairs-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'PredictAffairs/home.html', context)

def predictions(request):
    predicted_affairs = Data.objects.all()
    context = {
        'predicted_affairs': predicted_affairs
    }
    return render(request, 'PredictAffairs/predictions.html', context)