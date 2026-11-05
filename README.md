# resource_finder

Find your app's data files (sounds, DLLs, documentation) the same way whether you're running from source or from a frozen py2exe or py2app build.

## Install

```bash
pip install platform_utils git+https://github.com/accessibleapps/resource_finder.git
```

`resource_finder` imports [platform_utils](https://github.com/accessibleapps/platform_utils), but its `setup.py` doesn't list it yet, so install both as shown above.

## Use it

```python
from resource_finder import find_application_resource, ResourceNotFoundError

sound = find_application_resource("startup.ogg", "sounds")
dll = find_application_resource("bass.dll", ["lib", "x86"])
```

`find_application_resource(resource_name, extra_path='')` returns the full path to the file:

- In a frozen build, it looks in the bundled data folder (`platform_utils.paths.embedded_data_path()`).
- From source, it looks in the directory of the module that called it (found by walking up the call stack).
- `extra_path` is a subfolder, given as a string or as a list of folder names.
- If the file isn't there, it raises `ResourceNotFoundError` (a subclass of `IOError`) with the path it tried.

## License

MIT, per the classifier in `setup.py`.
