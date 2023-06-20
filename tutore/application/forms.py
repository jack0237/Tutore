from django import forms
from .models import Files


class FilesForm(forms.Form):

    class Meta:
        model = Files
        fields = ('title',
                  'image',
                  'sub_category',
                  'Auteur', 
                  'date_added',
                  'description', 
                  'date_de_modification', 
                  'dernier_contributeur' )
        labels = {
            'title':' Name',
            'sub_category':'Repertoir',
            'date_de_modification':'Date modif',
            'dernier_contributeur' : 'Contributor'
        }

    