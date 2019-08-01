from setuptools import find_packages, setup


def read_requirements(filename="requirements.txt"):
    return [ line.strip() for line in open(filename) if line.strip() and line[0].strip() != '#' ]


VERSION = '2017.8.16'

setup(
    name='django-gabrielson-templates',
    version=VERSION,
    author='Dave Gabrielson',
    author_email='Dave.Gabrielson@Gmail.Com',
    description='Standard templates for my person site.',
    url="http://gabrielson.ca/",
    license="(various)",
    packages=find_packages(exclude=['demo_site']),
    install_requires=read_requirements(),
    zip_safe=False,
    include_package_data=True,
)
