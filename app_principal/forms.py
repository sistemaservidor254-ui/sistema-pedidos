from django import forms


class ImportarNFeForm(forms.Form):
    arquivo_xml = forms.FileField(label="Arquivo XML da NF-e")
