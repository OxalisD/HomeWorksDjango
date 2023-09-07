from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        check = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                check += 1
        if check == 1:
            return super().clean()
        if check > 1:
            raise ValidationError('Основным может быть только один раздел')
        else:
            print(check)
            raise ValidationError('Укажите основной раздел')
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ScopeInline,)

