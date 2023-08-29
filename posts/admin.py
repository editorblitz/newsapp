from django import forms
from django.contrib import admin
from .models import Post, Tag, HomepageSection, HomepageSectionOrder

class PostAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Post
        fields = '__all__'

# Create a custom admin class using the above form
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title" ,)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(HomepageSection)
admin.site.register(HomepageSectionOrder)

