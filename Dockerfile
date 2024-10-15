# Start from python bookworm debian base image
FROM python:3.9-bookworm

# Set environment variables || don't check versions, don't write .pyc files, show output
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create working app directory
WORKDIR /usr/src/dogapi

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for access
EXPOSE 8000

# Run application
CMD ["./migrations.sh"]