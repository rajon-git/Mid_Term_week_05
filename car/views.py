# car/views.py

from django.views.generic import DetailView
from . import models  # Adjust import based on your project structure
from . import forms
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

class CarDetailsView(DetailView):
    model = models.Car
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'

    def post(self,request,*args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@login_required
def purchase_car(request, car_id):
    car = get_object_or_404(models.Car, pk=car_id)
    error_message = None
    if request.method == 'POST':
        form = forms.PurchaseForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if car.quantity >= quantity:
                total_price = car.price * quantity
                order = models.Order.objects.create(
                    user=request.user,
                    total_price=total_price,
                    cars = car
                )
                # order.cars.add(car)  
                car.quantity -= quantity
                car.save()
                return redirect('profile')  
            else:
                error_message = "Insufficient stock for this car."
    else:
        form = forms.PurchaseForm(initial={'car_id': car_id})
    context = {
        'car': car,
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'purchase_car.html', context)
