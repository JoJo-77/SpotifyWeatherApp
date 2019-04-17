from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import StrictButton

class zipform(forms.Form):
	zipcode = forms.CharField(max_length = 5)
	def __init__(self, *args, **kwargs):
		super(zipform, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = "zipCodeSubmit"
		self.helper.form_class = "form-horizontal"
		self.label_class = 'col-lg-2'
		self.field_class = 'col-lg-8'
		self.helper.layout = Layout(
			'Zipcode',
			StrictButton('Submit', css_class='btn-default'),
		)
		
		#self.helper.add_input(Submit('submit', 'Submit'))

	def clean(self):
		cleaned_data = super(zipform,self).clean()
		zipcode = cleaned_data.get('zipcode')
		if not zipcode:
			raise forms.ValidationError('Try entering something in!')