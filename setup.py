from distutils.core import setup
setup(
  name = 'rlsa_python',         # How you named your package folder (MyLib)
  packages = ['rlsa_python'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implementation of the Run Length Smoothing Algorithm (RLSA) in python',   # Give a short description about your library
  author = 'Luiz Fernando Lemos do Valle',                   # Type in your name
  author_email = 'lld2131@columbia.edu',      # Type in your E-Mail
  url = 'https://github.com/Lufeva123/rlsa_python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Lufeva123/rlsa_python/archive/v01.tar.gz',    # I explain this later on
  keywords = ['computer vision', 'image processing'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)