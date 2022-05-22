from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]



class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=(), coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        quantity_choices = kwargs.pop('quantity_choices', ())
        super().__init__(*args, **kwargs)
        self.fields['quantity'].choices = quantity_choices

    # def clean_quantity(self):
    #     if not self['quantity'].html_name in self.data:
    #         return self.fields['quantity'].initial
    #     return self.cleaned_data['quantity']

    # def clean_email_address(self):
    #     email = self.cleaned_data.get('email_address')
    #
    #     if self and self.user.email == email:
    #         return email
    #
    #     if UserProfile.objects.filter(email=email).count():
    #         raise forms.ValidationError(
    #             u'That email address already exists.'
    #         )
    #
    #     return email