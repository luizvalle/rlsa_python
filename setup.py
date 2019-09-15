from distutils.core import setup
setup(
  name = 'rlsa_python',
  packages = ['rlsa_python'],
  version = '0.1',
  license='MIT',
  description = 'Implementation of the Run Length Smoothing Algorithm (RLSA) in python',
  author = 'Luiz Fernando Lemos do Valle',
  author_email = 'lld2131@columbia.edu',
  url = 'https://github.com/Lufeva123/rlsa_python',
  download_url = 'https://github.com/Lufeva123/rlsa_python/archive/v0.1.tar.gz',
  keywords = ['computer vision', 'image processing'],
  install_requires=[
          'numpy'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
