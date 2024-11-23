from setuptools import setup, find_packages

setup(
    name='rpdvalidator',
    version="1.0.1",
    packages=find_packages(),
    install_requires=['jsonpath-ng', 'jsonschema', 'referencing'],
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
            'validateRPD=rpdvalidator.main:cli',
        ],
    },
    python_requires='>=3.7',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
