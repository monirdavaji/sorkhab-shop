from django import forms




class UserOrderForm(forms.Form):

    product_id = forms.IntegerField(widget=forms.HiddenInput())
    count = forms.IntegerField(widget=forms.NumberInput(),initial=1,min_value=1)
