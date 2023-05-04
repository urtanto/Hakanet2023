from django import forms
from django.forms import FileInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from main.models import TimeType, DirtType, StuffType, ProductType, Article


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
    name = forms.CharField(label="Название типа изделия",
                           max_length=255,
                           widget=TextInput(attrs={"class": "form-control"}))


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['type']


class StuffCreateForm(forms.Form):
    name = forms.CharField(label="Название типа материала",
                           max_length=255,
                           widget=TextInput(attrs={"class": "form-control"}))


class StuffEditForm(forms.ModelForm):
    class Meta:
        model = StuffType
        fields = ['type']


class DirtCreateForm(forms.Form):
    name = forms.CharField(label="Название типа загрязненности",
                           max_length=255,
                           widget=TextInput(attrs={"class": "form-control"}))


class DirtEditForm(forms.ModelForm):
    class Meta:
        model = DirtType
        fields = ['type']


class TimeCreateForm(forms.Form):
    name = forms.CharField(label="Название типа срочности",
                           max_length=255,
                           widget=TextInput(attrs={"class": "form-control"}))


class TimeEditForm(forms.ModelForm):
    class Meta:
        model = TimeType
        fields = ['type']


class ArticleCreateForm(forms.Form):
    name = forms.CharField(label="Название статьи",
                           max_length=255,
                           widget=TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(label="Статья",
                           widget=forms.Textarea())


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text']
