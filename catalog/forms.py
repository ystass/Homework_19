from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #exclude = ('created_at', 'updated_at')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for obj in prohibited_products:
            if obj in cleaned_data:
                raise forms.ValidationError("Такой продукт нельзя создать")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for obj in prohibited_products:
            if obj in cleaned_data:
                raise forms.ValidationError("Такой продукт нельзя создать")

        return cleaned_data
