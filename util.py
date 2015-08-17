import os

from django.conf import settings
from django.http import Http404

import markdown

def expand_markdown_path(uri):
    """Resolves URI path to the absolute filesystem path of the
    corresponding Markdown file.
    """
    if uri.endswith(os.sep):
        raise ValueError("Cannot parse a directory.")
    
    return os.path.join(settings.MARKDOWN_PAGES_ROOT, uri + '.md')

def markdown_or_404(uri):
    """Returns string from the Markdown file 
    corresponding to this URI.

    If no corresponding Markdown file is found, throw a 404 error.
    """
    path = expand_markdown_path(uri)
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return f.read()
    else:
        raise Http404

def parse_markdown_or_404(uri):
    """Parses markdown for URI or returns 404."""

    markdown_text = markdown_or_404(uri)
    html = markdown.markdown(markdown_text, output_format='html5', enable_attributes=False)

    return html
