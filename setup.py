from setuptools import setup

setup(
    name='django-rest-tests',
    version='0.5.3b',
    url='http://github.com/baseclue/django-rest-tests',
    license='Apache 2.0',
    author='Jan Češpivo',
    author_email='jan.cespivo@gmail.com',
    description='Semi-automated testing for Django REST framework API',
    packages=['rest_tests'],
    install_requires=["django", "djangorestframework"],
    test_requires=["pytest", "pytest-django"]
)
