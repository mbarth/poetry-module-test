"""
This is the `server_shared` module.

Include detailed description of the package, explaining its purpose and usage.
You can include examples, guidelines, or any relevant information for the users of this package.

Available submodules:
- db: Contains functionalities related to ...
- redis: Provides classes and functions for ...

Example usage:
from server_shared import SharedClass, shared_function
"""

# Import key classes and functions from submodules for easy access
from .db.module1 import SharedClass, shared_function
from .redis.redis_client import RedisClient

# Define what should be available at package level
__all__ = ["SharedClass", "shared_function", "RedisClient"]

# Can also include any package-level constants, variables or initialization code here