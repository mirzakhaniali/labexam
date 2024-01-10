# views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def create_model_instance(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or any other view
    else:
        form = MyModelForm()

    return render(request, 'create_model.html', {'form': form})
# views.py
from django.shortcuts import render
from .models import UserInput

def user_inputs(request):
    inputs = UserInput.objects.all()
    return render(request, 'user_inputs.html', {'inputs': inputs})
