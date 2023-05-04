from django import forms
from django.forms import FileInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from main.models import TimeType, DirtType, StuffType, ProductType


class PhotoUploadForm(forms.Form):
    def __init__(self,
                 type_product_choices,
                 type_stuff_choices,
                 type_dirt_choices,
                 *args, **kwargs):
        super(PhotoUploadForm, self).__init__(*args, **kwargs)
        self.fields['type_product'].choices = type_product_choices
        self.fields['type_stuff'].choices = type_stuff_choices
        self.fields['type_dirt'].choices = type_dirt_choices

    image1 = forms.ImageField(required=True, widget=FileInput(attrs={
        "onchange": "change_name(this)",
        "class": "",
    }))
    image2 = forms.ImageField(required=True, widget=FileInput(attrs={"onchange": "change_name(this)"}))
    type_product = forms.ChoiceField(label="Тип изделия", widget=forms.RadioSelect(), choices=())
    type_stuff = forms.ChoiceField(label="Тип материала", widget=forms.RadioSelect(), choices=())
    type_dirt = forms.ChoiceField(label="Тип загрязнения", widget=forms.RadioSelect(), choices=())


class ProductCreateForm(forms.Form):
    name = forms.CharField(label="Название изделия",
                           max_length=255,
                           widget=TextInput(attrs={"class": "form-control"}))


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['type']
