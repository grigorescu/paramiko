# Obtain shared config values
import sys
import os
from os.path import abspath, join, dirname

sys.path.append(abspath(join(dirname(__file__), '..')))
from shared_conf import *

# Releases changelog extension
extensions.append('releases')
releases_release_uri = "https://github.com/paramiko/paramiko/tree/%s"
releases_issue_uri = "https://github.com/paramiko/paramiko/issues/%s"

# Default is 'local' building, but reference the public docs site when building
# under RTD.
target = join(dirname(__file__), '..', 'docs', '_build')
if os.environ.get('READTHEDOCS') == 'True':
    target = 'http://docs.paramiko.org/en/latest/'
intersphinx_mapping['docs'] = (target, None)

# Sister-site links to API docs
html_theme_options['extra_nav_links'] = {
    "API Docs": 'http://docs.paramiko.org',
}
