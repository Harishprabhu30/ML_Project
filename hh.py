import sys

# Print the current sys.path
print(sys.path)

# Remove a path from sys.path
if '/path/to/custom/directory' in sys.path:
    sys.path.remove('/path/to/custom/directory')
