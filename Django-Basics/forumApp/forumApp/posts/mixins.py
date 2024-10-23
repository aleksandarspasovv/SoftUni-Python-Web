from django import forms


class DisabledRequiredFields(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        for field, field_name in self.fields.items():
            if self.disabled_fields[0] == '__all__' or field_name in self.disabled_fields:
                field.disabled = True
