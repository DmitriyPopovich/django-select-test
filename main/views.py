from django.shortcuts import render, redirect
from main.forms import SelectorForm
from main.services import ApiService
from main.utils import get_initial, get_kwargs, prepare_api_data

api_service = ApiService()


def index(request, brand=None, service=None, style=None):
    parse = api_service.get_data('parse_link', brand, service, style)
    initial = get_initial(parse)
    form = SelectorForm(initial)
    context = {'form': form}
    if request.POST:
        kwargs = get_kwargs(request)
        return redirect('main:index', **kwargs)
    return render(request, 'main/index.html', context)




