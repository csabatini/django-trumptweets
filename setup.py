import os
from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*/*.pyc '
                  './*/*/*.pyc ./*.tgz ./*.egg-info ./*/__pycache__ ./*/*/__pycache__ ./.eggs ./.cache')


setup(name='django-trumptweets',
      version='0.0.0',
      description='Simple django project to consume the TrumpTweets API',
      url='https://github.com/csabatini/django-trumptweets',
      author='Caleb Sabatini',
      author_email='calebsabatini@gmail.com',
      packages=find_packages(),
      install_requires=[
          'Django==1.8.11',
          'django-compressor==2.1.1',
          'requests==2.9.1'
      ],
      setup_requires=[
          'pytest-runner==2.11.1'
      ],
      test_suite='pytest',
      tests_require=[
          'pytest==3.0.7',
          'pytest-django==2.9.1',
          'mockito==1.0.11'
      ],
      zip_safe=False,
      cmdclass={
          'clean': CleanCommand
      })
