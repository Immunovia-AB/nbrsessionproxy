import setuptools

setuptools.setup(
    name="nbrsessionproxy",
    version='0.1.0',
    url="https://github.com/Immunovia-AB/proxy",
    description="Jupyter extension to proxy RStudio's rsession",
    packages=setuptools.find_packages(),
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'notebook',
        'nbserverproxy >= 0.8.3'
    ],
    package_data={'nbrsessionproxy': ['static/*']},
)
