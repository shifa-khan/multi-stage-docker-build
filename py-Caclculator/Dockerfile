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

############################################
# HERE STARTS THE MAGIC OF MULTI STAGE BUILD
############################################

FROM gcr.io/distroless/python3-debian11

# Set the working directory in the distroless image
WORKDIR /app

# Copy the application files from the build stage
COPY --from=build /app /app

# Set the entrypoint for the container to run the Python application
ENTRYPOINT ["python3", "your_app.py"]
