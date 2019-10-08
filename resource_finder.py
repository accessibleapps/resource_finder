import os
from platform_utils.paths import module_path, is_frozen, embedded_data_path
from six import string_types 

class ResourceNotFoundError(IOError): pass

def find_application_resource(resource_name, extra_path=''):
 if not isinstance(extra_path, string_types):
  extra_path = os.path.join(*extra_path)
 if is_frozen():
  base_path = embedded_data_path()
 else:
  base_path = module_path(3)
 path = os.path.join(base_path, extra_path, resource_name)
 if not os.path.exists(path):
  raise ResourceNotFoundError("Could not find application resource %r" % path)
 return path
