# main.py in the root directory
from server_shared import SharedClass, shared_function

# Create an instance of SharedClass
shared_instance = SharedClass("[Root App User]")
print(shared_instance.greet())

# Use the shared_function
result = shared_function(3, 7)
print(f"From main; The sum is: {result}")
