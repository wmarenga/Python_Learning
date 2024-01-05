# With this template we can import files from other modules.

from package1.module1 import variable1
variable2 = 'variable2'

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
                # ../../ (previous two folders = above)
            )
        )
    )
except ImportError:
    raise
