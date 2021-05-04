from setuptools import setup

setup(name='everysk',
      packages=['everysk', 'everysk.api_resources'],
      package_data={'everysk': ['*.crt']},
      version='1.0.2',
      description='Python client for Everysk API',
      author='Everysk Technologies',
      author_email='contact@everysk.com',
      url='https://github.com/Everysk/Everysk-API-Python',
      install_requires=['requests', 'setuptools'],
      keywords=['everysk'],
      license='MIT',
      zip_safe=False)