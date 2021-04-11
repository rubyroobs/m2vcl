from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='m2vcl',
    version='0.0.1',
    description='Export statistical models to VCL, for the Varnish cache.',
    url='https://github.com/rubyroobs/m2vcl',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ruby Nealon',
    author_email='ruby@ruby.sh',
    packages=['m2vcl', 'm2vcl.vcl'],
    python_requires=">=3.6",
    install_requires=[
        "m2cgen",
    ],
    extras_require={
        'test': ['scikit-learn', 'numpy'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/rubyroobs/m2vcl/issues',
    },
)
