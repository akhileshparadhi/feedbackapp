from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.




def create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    form = FeedbackForm()

    return render(request, 'sample_project/index.html', {'form': form})

def show(request):
    feedbacks = Feedback.objects.all()
    return render(request, "sample_project/show.html", {'feedbacks': feedbacks})

