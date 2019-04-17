from django import forms

class zipform(forms.Form):
	zipcode = forms.CharField(max_length = 5)

	def clean(self):
		cleaned_data = super(zipform,self).clean()
		zipcode = cleaned_data.get('zipcode')
		if not zipcode:
			raise forms.ValidationError('Try entering something in!')