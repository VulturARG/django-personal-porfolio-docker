from django.contrib import admin
from .models import Project, WebPage, Skill, City


class WebPageAdmin(admin.ModelAdmin):
    fields       = ['web_page','title','description','is_menu_item']
    list_display = ['web_page','title','description','is_menu_item']

admin.site.register(WebPage,WebPageAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    fields       = ['title','summary','description','technology','start_date','finish_date','image_path']
    list_display = ['title','summary','technology','start_date','image_path']
    ordering     = ['-start_date']

admin.site.register(Project,ProjectsAdmin)

class SkillsAdmin(admin.ModelAdmin):
    fields       = ['title','description','order']
    list_display = ['title','description','order']
    ordering     = ['-order']

admin.site.register(Skill,SkillsAdmin)

admin.site.register(City)
