from setuptools import setup, find_packages

setup(
    name='vdist',
    version='1.0',
    description='Create OS packages from Python '
                'projects using Docker containers',
    long_description='Create OS packages from Python '
                     'projects using Docker containers',
    author='L. Brouwer',
    author_email='objectified@gmail.com',
    license='MIT',
    url='https://github.com/objectified/vdist',
    packages=find_packages(),
    install_requires=['jinja2==2.7.3'],
    entry_points={'console_scripts': ['vdist=vdist.vdist_launcher:main', ], },
    package_data={'': ['internal_profiles.json', '*.sh']},
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False,
    keywords='python docker deployment packaging',
)
