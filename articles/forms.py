from django import forms
from .models import Article


class DateInput(forms.DateInput):
    input_type = "date"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["date", "title", "content", "incoming", "spending"]
        widgets = {"date": DateInput()}
        labels = {
            "date": "날짜",
            "title": "내용",
            "content": "메모",
            "incoming": "수입",
            "spending": "지출",
        }
