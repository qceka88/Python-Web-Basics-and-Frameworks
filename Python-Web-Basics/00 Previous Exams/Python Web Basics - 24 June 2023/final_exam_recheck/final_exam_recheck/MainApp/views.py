from django.shortcuts import render
from final_exam_recheck.ProfileApp.models import ProfileModel
from final_exam_recheck.FruitApp.models import FruitModel


# Create your views here.
def index(request):
    data = {
        'not_registered_user': False if find_profile() else True,
    }
    return render(request, 'core/index.html', data)


def dashboard(request):
    fruits = FruitModel.objects.all().order_by('pk')
    data = {
        'fruit_list': fruits,
    }
    return render(request, 'core/dashboard.html', data)


def find_profile():
    try:
        return ProfileModel.objects.all().first()
    except ProfileModel.DoesNotExist:
        return None
