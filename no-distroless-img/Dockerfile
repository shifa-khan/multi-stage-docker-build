###########################################
# BASE IMAGE
###########################################

FROM registry.access.redhat.com/ubi8/ubi AS build

# Install Python
RUN yum update -y && \
    yum install -y python3

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

ENTRYPOINT ["python3", "calc.py"]
