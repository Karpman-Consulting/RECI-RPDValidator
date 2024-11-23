from setuptools import setup, find_packages

setup(
    name='rpdvalidator',
    version="1.0",
    packages=find_packages(),
    install_requires=['jsonpath2', 'jsonschema'],
    url='https://github.com/Karpman-Consulting/RECI-RPDValidator',
    author='Jackson Jarboe',
    author_email='jackson@karpmanconsulting.net',
    description='A Python tool for validating RPD files according to a specified version of the ASHRAE 229 schema.',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    package_data={
            "rpdvalidator.schema_versions": [
                "**/*.json"
            ]
        },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'validateRPD=rpdvalidator.main:run',
        ],
    },
    python_requires='>=3.7',
)
