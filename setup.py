from setuptools import setup, find_packages

setup(
    name='wikipathway2genes',
    version='0.0.4',
    author='Pr (France) Dr. rer. nat. Vijay K. ULAGANATHAN',
    author_email=' ',
    description='A package to convert WikiPathways IDs to genes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wikipathway2genes=wp2genes.wp2genes:main',
        ],
    },
    install_requires=[
        'argparse',
        'pywikipathways',
    ],
)

