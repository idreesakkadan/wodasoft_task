from django import forms
from .models import Article
from django.conf import settings


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        ins = kwargs.get('instance', None)
        super(ArticleForm, self).__init__(*args, **kwargs)
        title = {}
        if ins:
            title = ins.title
        for i in settings.LANGUAGES:
            field_name = 'article_title_(%s)' % (i[0])
            is_required = False if not i[0] == 'en' else True
            self.base_fields[field_name] = forms.CharField(
                initial=title.get(i[0], ''), required=is_required
            )
            self.fields[field_name] = forms.CharField(
                initial=title.get(i[0], ''), required=is_required
            )

    def save(self, commit: bool = True):
        instance = super(ArticleForm, self).save(commit=False)
        out = {}
        for i in settings.LANGUAGES:
            field_name = 'article_title_(%s)' % (i[0],)
            extra_field = self.cleaned_data.get(field_name, None)
            out[i[0]] = extra_field
        instance.title = out
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Article
        exclude = ['title']
