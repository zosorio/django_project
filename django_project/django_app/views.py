from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request=request, template_name="django_app/car_list.html")