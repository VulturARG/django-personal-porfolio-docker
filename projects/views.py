from django.shortcuts import render
from .models import Project, WebPage, Skill, City
from django.http import HttpResponse
import json
from django.views.generic import View


def index(request):
    index = WebPage.objects.get(web_page='index')
    menu_items = WebPage.objects.all().filter(is_menu_item=True)
    context = {
        'welcome': index,
        'menu_items': menu_items,
    }
    return render(request, 'projects/index.html', context)


def project_index(request):
    projects = Project.objects.all()
    menu_items = WebPage.objects.all().filter(is_menu_item=True)
    context = {
        'projects': projects,
        'menu_items': menu_items,
    }
    return render(request, 'projects/project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    menu_items = WebPage.objects.all().filter(is_menu_item=True)
    context = {
        'project': project,
        'menu_items': menu_items,
    }
    return render(request, 'projects/project_detail.html', context)


def skill_index(request):
    skill_titles = WebPage.objects.get(web_page='skills')
    skills = Skill.objects.all()
    menu_items = WebPage.objects.all().filter(is_menu_item=True)
    context = {
        'skills': skills,
        'skill_titles': skill_titles,
        'menu_items': menu_items,
    }
    return render(request, 'projects/skill_index.html', context)


def generic_page(request, pk):
    generic_page = WebPage.objects.get(pk=pk)
    menu_items = WebPage.objects.all().filter(is_menu_item=True)
    context = {
        'generic_page': generic_page,
        'menu_items': menu_items,
    }
    return render(request, 'projects/generic_page.html', context)


def ajax_example(request):
    menu_items = WebPage.objects.all().filter(is_menu_item=True)
    context = {
        'menu_items': menu_items,
    }
    return render(request, 'projects/ajax.html', context)


class SearchCity(View):

    def get(self, request):
        if request.is_ajax:
            search_term = request.GET.get('term', '')
            city = City.objects.filter(name__icontains = search_term)[0:10]
            results = []
            for an in city:
                data = {}
                data['label'] = an.name
                results.append(data)
            data_json = json.dumps(results)
        else:
            data_json = "failure"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
    
    
class SearchExtraData(View):

    def get(self, request):
        if request.is_ajax:
            search_term = request.GET.get('term', '')
            datos = City.objects.filter(name__icontains = search_term)
            results = []
            data = {}
            for dato in datos:
                data = {}
                data['label'] = dato.name
                data['zip'] = dato.zip_code
                data['name'] = dato.province.name
                results.append(data)
            data_json = json.dumps(results)
        else:
            data_json = "failure"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
