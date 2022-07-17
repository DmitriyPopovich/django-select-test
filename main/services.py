import requests

from djangotest.settings import API_URL

ENDPOINTS = [
    "brands_terms",
    "parse_link",
    "styles",
    "terms",
]


def _validate(endpoint):
    if endpoint not in ENDPOINTS:
        raise ValueError("Unknown API endpoint '{}'".format(endpoint))
    return None


def _call_api(endpoint, *args):
    url = _api_url_build(endpoint, *args)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def _build_get_param(item):
    part = item.split("-", 1)[1]
    type_s = item.split("-", 1)[0]
    result = ""
    if type_s == "s":
        result += "service_slug="
    elif type_s == "b":
        result += "brand_slug="
    elif type_s == "st":
        result += "style_slug="
    return result+part+"&"


def _api_url_build(endpoint, *args):
    host = "".join([API_URL, endpoint, "/"])
    if args:
        host += "?"
        for item in args:
            if item:
                param = _build_get_param(item)
                host += param
        if host[-1] == "&":
            host = host[:-1]
    return host


def get_data(endpoint, *args):
    _validate(endpoint)
    data = _call_api(endpoint, *args)
    return data