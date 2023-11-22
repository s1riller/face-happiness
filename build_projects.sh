#!/bin/bash

# Скрипт для сборки проектов в папках Luminex-Front-2 и Luminex-Back с использованием Docker

echo "Building and running Luminex-Front-2..."
cd Luminex-Front-2
docker-compose up --build -d
cd ..

# Сборка и запуск проекта в Luminex-Back
echo "Building and running Luminex-Back..."
cd Luminex-Back
docker-compose up --build -d
cd ..

echo "Projects built and running successfully."
