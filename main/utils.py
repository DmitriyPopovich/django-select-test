

def prepare_api_data(data):
    res = list()
    res.append(('', '--------'))
    for item in data:
        tmp = (item['slug'], item['label'])
        res.append(tmp)
    return res


def get_initial(data):
    initial = dict()
    if data['brand']:
        initial['brands'] = data['brand']['slug']
    if data['service']:
        initial['terms'] = data['service']['slug']
    if data['style']:
        initial['styles'] = data['style']['slug']
    return initial


def get_kwargs(request):
    kwargs = dict()
    if request.POST['brands']:
        kwargs["brand"] = 'b-'+request.POST['brands']
    if request.POST['terms']:
        kwargs["service"] = 's-'+request.POST['terms']
    if request.POST['styles']:
        kwargs["style"] = 'st-'+request.POST['styles']
    return kwargs
