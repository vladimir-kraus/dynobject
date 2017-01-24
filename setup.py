from setuptools import setup, find_packages

exec(open("dynobject/__init__.py").read())

setup(
    name='dynobject',
    version=__version__,
    author='Vladimir Kraus',
    author_email='vladimir.kraus@gmail.com',
    packages=find_packages(),
    url='http://github.com/vladimir-kraus/dynobject',
    license='MIT',
    description='DynObject class which allows dynamic adding of attributes '
                'on the run and dict-like access to the attributes.',
    long_description=open('README.md').read(),
    include_package_data=True,
    setup_requires=[],
    install_requires=[],
    keywords=['dynamic', 'object', 'attribute', 'dict', 'attrdict'],
    classifiers=[],
    test_suite='nose.collector',
    tests_require=['nose']
)
