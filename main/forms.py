from django import forms

from main.services import get_data
from main.utils import prepare_api_data


class SelectorForm(forms.Form):

    brands_data = prepare_api_data(get_data('brands_terms')['data'])
    terms_data = prepare_api_data(get_data('terms')['data'])
    styles_data = prepare_api_data(get_data('styles')['data'])

    brands = forms.ChoiceField(
        choices=brands_data,
        required=False,
        widget=forms.Select(attrs={'onchange': 'submit();'})
    )
    terms = forms.ChoiceField(
        choices=terms_data,
        required=False,
        widget=forms.Select(attrs={'onchange': 'submit();'})
    )
    styles = forms.ChoiceField(
        choices=styles_data,
        required=False,
        widget=forms.Select(attrs={'onchange': 'submit();'})
    )
