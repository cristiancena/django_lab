from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Tu e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

class addBooksPublisher(forms.Form):
	name 			= forms.CharField(widget=forms.TextInput())
	address			= forms.CharField(widget=forms.TextInput())
	city 			= forms.CharField(widget=forms.TextInput())
	state_province 	= forms.CharField(widget=forms.TextInput())
	country 		= forms.CharField(widget=forms.TextInput())
	website 		= forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data #retorna informacion validada x django p que el usuario no pueda poner cualquier cosa en la db