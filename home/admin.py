from django.contrib import admin
from .models import Project, ProjectImage, Tag

from django.utils.html import format_html

admin.site.register(Tag)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'detail_url')
    filter_horizontal = ('tags',)
    inlines = [ProjectImageInline]
    search_fields = ['title']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)  # Optional: for direct access
