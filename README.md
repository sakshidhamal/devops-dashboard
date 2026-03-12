# DevOps Server Health Dashboard

## Project Description
This project is a DevOps-based server monitoring dashboard built using Flask.  
It displays real-time CPU, memory, and disk usage of the system.

## Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript
- Docker
- Git
- GitHub
- GitHub Actions (CI/CD)

## Features
- Real-time system monitoring
- Docker containerization
- Version control using Git
- CI pipeline using GitHub Actions

## How to Run the Project

### Run locally
python app.py

Open:
http://localhost:5000

### Run using Docker
docker build -t devops-dashboard .
docker run -p 5000:5000 devops-dashboard