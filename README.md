# Python Calculator with Distroless Image

This project is a simple Python calculator implemented in a Docker container using a distroless Python image. The calculator allows users to input numbers and select various mathematical operations to perform, such as addition, subtraction, multiplication, and division.

## Features
- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Utilizes a minimalistic distroless Python image for reduced attack surface and improved security.
- Distroless images minimize the size of Docker images by including only the necessary dependencies to run the application, resulting in smaller image sizes compared to traditional base images. This particular image reduced the size from 236MB to 52.6MB
- Reduced image size translates to faster deployment times and reduced storage costs in container registries.
- Enhanced security: Distroless images remove unnecessary OS packages and utilities, reducing the potential attack surface and limiting the impact of security vulnerabilities.

## Technologies Used
- Python
- Docker
- Distroless

## How to Use
1. Clone the repository.
2. Build the Docker image.
3. Run the Docker container.

Feel free to contribute, report issues, or suggest enhancements!
