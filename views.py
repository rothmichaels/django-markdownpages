import re

from django.shortcuts import render
from django.conf import settings

from django.http import HttpResponse
from django.template import RequestContext, loader

from .util import parse_markdown_or_404

# Create your views here.
def root(request):
    return page(request, 'index')

def index(request, markdown_path):
    path = markdown_path + 'index'
    return page(request, path)
    
def page(request, markdown_path):
    markdown = parse_markdown_or_404(markdown_path)
    search = re.findall('^(.*)<title>(.*)</title>(.*)$',markdown,re.DOTALL)
    title = None
    if len(search) > 0 and len(search[0]) == 3:
        print(search)
        search = search[0]
        title = search[1]
        markdown = search[0] + search[2]
    
    template = loader.get_template('markdownpages/page.html')
    context = RequestContext(request, {
        'markdown_title': title,
        'markdown_body': markdown,
    })

    return HttpResponse(template.render(context))
