# from http://stackoverflow.com/a/600612

import errno    
import os

def mkdir_p(paths):
    for path in paths:
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise