from django import forms
import random

from .models import World

class WorldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorldForm, self).__init__(*args, **kwargs)

        colours = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan', 'indigo', 'gold', 'silver', 'bronze']
        geological = ['fields', 'forest', 'coast', 'penisula', 'plateau', 'canyon', 'escarpment', 'desert', 'island']
        rand_name = colours[random.randint(0, len(colours)-1)] + ' ' + geological[random.randint(0, len(geological)-1)]
        self.fields['name'].initial = rand_name.title()

    class Meta:
        model = World
        fields = [
            'name',
            'width',
            'height'
        ]
