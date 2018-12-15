
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'yaml path',
    'author': 'hejack0207',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'hejack0207@sina.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['yamlpath'],
    'scripts': [],
    'name': 'yamlpath'
    'entry_points': {"console_script": ["yamlpaths=yamlpath.cli:main"]}
}

setup(**config)
