from django.shortcuts import render, get_object_or_404, redirect

from django_models_exercise.shipyard.models import Worker, Department, WorkerAddress


# Create your views here.
def index(request):
    workers_list = Worker.objects.all()

    workers_young = Worker.objects.filter(worker_age__lt=35)
    workers_old = Worker.objects.filter(worker_age__gt=35)

    context = {
        'workers': workers_list,
        'workers2': workers_young,
        'workers3': workers_old,
    }

    return render(request, 'shipyard/index.html', context)


def worker_details(request, pk):
    worker = Worker.objects.get(pk=pk)

    data = {
        'worker': worker
    }

    return render(request, 'shipyard/details.html', data)


def delete_worker(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    worker.delete()

    return redirect('index')


def departments_index(request):
    departments_list = Department.objects.all()

    data = {
        'departments': departments_list
    }

    return render(request, 'shipyard/departments_index.html', data)


def department_details(request, slug):
    dep = get_object_or_404(Department, slug=slug)

    data = {
        'department': dep
    }
    return render(request, 'shipyard/department_details.html', data)


def address_book(request):
    address_list = WorkerAddress.objects.all()

    data = {
        'addresses': address_list
    }
    return render(request, 'shipyard/address_book.html', data)


def address_details(request, slug):
    address = get_object_or_404(WorkerAddress, slug=slug)

    data = {
        'address_details': address
    }
    return render(request, 'shipyard/address_details.html', data)
