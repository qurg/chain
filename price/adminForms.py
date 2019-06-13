from django import forms


class InquireForm(forms.ModelForm):
    pass
    # remark = forms.CharField(widget=forms.Textarea, label='备注', required=False)


class QuoteForm(forms.ModelForm):
    pass