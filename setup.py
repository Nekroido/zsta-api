import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_openapi3',
    'pyramid_debugtoolbar',
    'waitress',
    'simplecalculator'
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(name='api',
      scripts=['bin/generate-specs-file'],
      version='0.0',
      description='Sample API project',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Nekroido',
      author_email='nekroido@windowslive.com',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = api:main
      """,
      )
