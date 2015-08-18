import os

from django.test import TestCase
from unittest.mock import Mock,mock_open,patch

from django.conf import settings
from django.http import Http404,HttpRequest

from . import util
from . import views
 
class UtilTests(TestCase):    
    """Test functions in django_markdown_pages.util"""

    TEST_MARKDOWN = '# Test Data\n\nhello, world'
    
    def setUp(self):
        self.previous_markdown_root = settings.MARKDOWN_PAGES_ROOT
        self.root  = os.path.join(settings.BASE_DIR,'/django_markdown_pages/test_data')
        settings.MARKDOWN_PAGES_ROOT = self.root

    def tearDown(self):
        settings.MARKDOWN_PAGES_ROOT = self.previous_markdown_root
            
    def test_expand_markdown_path_page(self):
        """Tests page resolution."""
        expected = self.root + '/page.md'
        self.assertEqual(util.expand_markdown_path('page'),expected)
        
    def test_expand_markdown_path_page_in_dir(self):
        """Test page resolution in a directory."""
        expected = self.root + '/testdir/page.md'
        self.assertEqual(util.expand_markdown_path('testdir/page'),expected)

    def test_expand_markdown_dir(self):
        """Should raise value exception."""
        self.assertRaises(ValueError, util.expand_markdown_path, 'testdir/')

    def test_parse_markdown(self):
        """Test parsing an existing Markdown file."""
        with patch('os.path.isfile',Mock(return_value=True)), \
             patch('builtins.open',mock_open(read_data=UtilTests.TEST_MARKDOWN)):
            text = util.markdown_or_404('testdir/page')
            self.assertEqual(text, UtilTests.TEST_MARKDOWN)

    def test_404(self):
        """Test 404 is thrown if no Markdown file is found."""
        with patch('os.path.isfile',Mock(return_value=False)):
            self.assertRaises(Http404, util.markdown_or_404, 'testdir/page')

class ViewsTests(TestCase):
    def setUp(self):
        self.mock_request = Mock(spec=HttpRequest)
        self.original_page_fn = views.page

    def tearDown(self):
        views.page = self.original_page_fn
            
        
    def test_root(self):
        """Test root(request,markdown_path) 
        calls page(request=request,markdown_path='index')."""
        page_mock = Mock()
        views.page = page_mock

        views.root(self.mock_request)

        page_mock.assert_called_with(self.mock_request, 'index')

        
    def test_index(self):
        """Test index(request,markdown_path) calls 
        page(request=request,markdown_path=(markdown_path+'index')."""
        page_mock = Mock()
        views.page = page_mock

        views.index(self.mock_request,'testdir/')

        page_mock.assert_called_with(self.mock_request, 'testdir/index')

        
    def test_page(self):
        """Test page loads correct view and populates correct markdown file."""

        
    def test_page_404(self):
        """Test a 404 is thrown for an unkown path."""

        
