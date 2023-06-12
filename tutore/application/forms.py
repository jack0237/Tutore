from django import forms
from .models import Files


class FilesForm(forms.Form):

    class Meta:
        model = Files
        fields = ('title',
                  'image',
                  'sub_category',
                  'Auteur', 
                  'description', 
                  'date_de_modification', 
                  'dernier_contributeur' )
        labels = {
            'title':' Name',
            'sub_category':'category'
        }

    def __init__(self, *args, **kwargs):
        super(FilesForm,self).__init__(*args, **kwargs)
        