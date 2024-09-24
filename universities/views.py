from django.http import response, Http404
from django.views.generic import ListView, DetailView

from .models import University
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def universities(request):
    universities = University.objects.all()[:20]
    return render(request, 'universities.html', {'universities': universities})


def university(request, id):
    university = get_object_or_404(University, pk=id)

    # try:
    #     university = University.objects.get(pk=id)
    # except University.DoesNotExist:
    #     return response.HttpResponse('Not found', status=404)

    # university = University.objects.filter(pk=id).first()
    if not university:
        raise Http404
        # return response.HttpResponse('Not found', status=404)
        # return response.HttpResponseNotFound('Not found')

    return render(request, 'university.html', {'university': university})


class UniversityListView(ListView):
    model = University
    paginate_by = 10
    template_name = 'universities_list.html'


class UniversityDetailView(DetailView):
    model = University
    template_name = 'university.html'
