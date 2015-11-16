Markdown Pages
==============

Markdown pages is a simple Django app to render a directory of Markdown
files as HTML.

Quick Start
-----------

1. Add "markdownpages" to your INSTALLED_APPS setting like this::

     INSTALLED_APPS = (
         ...
         'markdownpages',
     )

2. Add path to your markdown file directory to settings.py::

     MARKDOWN_PAGES_ROOT = '/path/to/your/markdown/directory'

3. Include the Markdown Pages URLConf in your project urls.py by adding
   the folowing as the final url in urlpatterns:

     url(r'^', include('markdownpages.urls'))

4. Start server!

License
-------
Copyright (c) 2015 Roth Michaels. Distributed under the Eclipse Public License v1.0.

