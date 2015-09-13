SOLID OPPINION PROJECT
==========
Change credentials before you run.

Tests for http://my.solidopinion.com/ site functionality.
To run you need to install Python 2.7, pytest, selenium, pytest-mozwebqa and dependencies.
The Windows command line string:
py.test --baseurl=https://my.solidopinion.com --driver=firefox --skipurlcheck so\tests\  --credentials=so\credentials.yaml
