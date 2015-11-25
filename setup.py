from distutils.core import setup

setup(
    name="python-tranquil",
    version="0.0.1",
    author="Nick Moore",
    author_email="nick@mnemote.com",
    url="https://github.com/mnemote/python-tranquil",
    description="Tranquil Python Implementation",
    keywords=["json", "ajax"],
    license='BSD',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    py_modules=['tranquil'],
)
