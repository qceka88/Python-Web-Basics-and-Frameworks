from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from class_based_views_exercise.WebCBV.models import Motorcycle


def some_test(request):
    context = {
        'bikes_list': Motorcycle.objects.all()
    }
    return render(request, 'web/base_view.html', context)


# Create your views here.
class IndexView(views.View):

    def get(self, request):
        context = {
            'bikes_list': Motorcycle.objects.all()
        }
        return render(request, 'web/base_view.html', context)


class TemplateView(views.TemplateView):
    template_name = 'web/template_view.html'

    def get_context_data(self, **kwargs):
        bikes_list = Motorcycle.objects.all()

        context = {
            'bikes_list': bikes_list
        }
        return context


class RedirectView(views.RedirectView):
    url = reverse_lazy('base view')


class ListView(views.ListView):
    model = Motorcycle
    template_name = 'web/list_motorcycles.html'
    paginate_by = 5


class DetailsView(views.DetailView):
    model = Motorcycle
    template_name = 'web/details_view.html'


class CreateView(views.CreateView):
    model = Motorcycle
    fields = '__all__'
    template_name = 'web/create_View.html'
    success_url = reverse_lazy('base view')


class UpdateView(views.UpdateView):
    model = Motorcycle
    fields = '__all__'
    template_name = 'web/update_view.html'
    success_url = reverse_lazy('base view')


class DeleteView(views.DeleteView):
    model = Motorcycle
    template_name = 'web/delete_view.html'
    success_url = reverse_lazy('base view')
    form_class = modelform_factory(
        Motorcycle,
        fields='__all__',
    )

    def get_form_kwargs(self):
        instance = self.get_object()
        form = super().get_form_kwargs()

        form.update(instance=instance)
        return form
