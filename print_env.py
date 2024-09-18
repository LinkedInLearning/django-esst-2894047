import os

print("Variables de entorno:")
for key, value in os.environ.items():
    print(f"{key}: {value}")
