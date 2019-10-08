from setuptools import setup

__version__ = "0.1"
__doc__ = """Basic resource finder package to let desktop apps find resources like dlls and datafiles they need both when running from source and not."""

setup(
 name = "resource_finder",
 version = __version__,
 description = __doc__,
 py_modules = ['resource_finder'],
 install_requires = ['six', ],
 zip_safe = False,
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
