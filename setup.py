from setuptools import setup

__version__ = "0.1"
__doc__ = """Find resources for desktop applications"""

setup(
 name = "resource_finder",
 version = __version__,
 description = __doc__,
 py_modules = ['resource_finder'],
 zip_safe = False,
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
