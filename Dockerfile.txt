# Use a Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /testpythonfiledirectory


# Copy the rest of the application code
COPY . .

# Specify the command to run the application
CMD ["python", "unit_test.py"]
