# MLOps Course with Streamlit Dockerized Application

This repository contains code and resources for a course on MLOps (Machine Learning Operations), focusing on building a Dockerized application with a client-server architecture using Streamlit for machine learning visualization.

![chrome-capture-2024-2-8](https://github.com/victorsigogneau/mlops-docker/assets/114923062/47560246-cc45-4720-8d32-e4b94fa66aef)


## Overview

MLOps is the practice of combining machine learning (ML) and operations to streamline the process of deploying, maintaining, and iterating on ML models. This course aims to provide a practical guide to MLOps principles and techniques through the development of a Dockerized application.

### Components

- **Client**: The client component consists of a Streamlit application that provides a user interface for interacting with the machine learning models.
- **Server**: The server component hosts the machine learning models and serves predictions to the client.

## Getting Started

To get started with the project, make sure you have Docker and Docker Compose installed on your machine.

### Prerequisites

- Docker installed on your machine: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose installed on your machine: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/victorsigogneau/mlops-docker.git
    cd mlops-docker
    ```

2. Build and run the Docker containers:

    ```bash
    docker compose up 
    ```

3. Access the Streamlit application in your browser:

    ```
    http://localhost:8501
    ```

## Usage

Once the Docker containers are running, you can interact with the Streamlit application by accessing it through your browser. Use the provided interface to make predictions with the machine learning models hosted on the server.


