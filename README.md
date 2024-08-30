# Microservices Deployment on AWS with Kubernetes and Helm

This repository contains a sample microservices application deployed on AWS using Kubernetes and Helm. It includes infrastructure provisioning with Terraform, application deployment with Helm, and CI/CD automation with Jenkins.

## Directory Structure

- **terraform/**: Contains Terraform configurations for provisioning AWS EKS cluster and related infrastructure.
- **inventory-service/**: Microservice for inventory management.
- **order-service/**: Microservice for order processing.
- **payment-service/**: Microservice for payment processing.
- **product-service/**: Microservice for product management.
- **user-service/**: Microservice for user management.
- **jenkins/**: Contains Jenkins pipeline configurations for CI/CD.
- **README.md**: This file with project overview and instructions.

## Prerequisites

Before you begin, ensure you have the following tools installed:

- [Terraform](https://www.terraform.io/downloads.html)
- [Docker](https://docs.docker.com/get-docker/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Jenkins](https://www.jenkins.io/download/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Setup Instructions

### 1. Version Control

1. Clone the repository:
   ```bash
   git clone https://github.com/Fayaz1898/Task1-Ecommerce.git
   cd Task1-Ecommerce

2. Infrastructure Provisioning with Terraform
    Navigate to the Terraform directory and initialize and apply terraform configurations to provision AWS EKS Cluster

    cd terraform
    terraform init
    terraform plan
    terraform apply 

3. Build and Push Docker Images

. Ensure Docker is running.
. Build and push Docker images for each microservice. 
    cd inventory-service
    docker build -t fayaz6202/inventory-service:latest .  (use your repo in place of fayaz6202 if you want to build in your repository)
    docker push fayaz6202/inventory-service:latest

. You can also use Jenkins to automate this step (see Jenkins file in directory)

4. Deploy Microservices with Helm
    
Install Helm charts for each microservice:

    helm upgrade --install inventory-service ./inventory-service/helm/inventory-service-chart
    helm upgrade --install order-service ./order-service/helm/order-service-chart
    helm upgrade --install payment-service ./payment-service/helm/payment-service-chart
    helm upgrade --install product-service ./product-service/helm/product-service-chart
    helm upgrade --install user-service ./user-service/helm/user-service-chart

5. Setup Jenkins CI/CD Pipeline

   Install Jenkins: Use the Jenkins installation guide to install Jenkins.

   Install Plugins: Ensure Jenkins has the following plugins installed:

    Git
    Docker
    Helm
    Terraform

Create a Pipeline Job:

Go to Jenkins dashboard and create a new Pipeline job.
Configure the job to use the Jenkinsfile located in the jenkins/ directory of this repository.
Configure Jenkins Credentials:

Add credentials for Docker Hub in Jenkins.







