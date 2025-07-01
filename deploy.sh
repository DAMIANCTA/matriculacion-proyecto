#!/bin/bash

echo "🔧 [1/6] Actualizando sistema e instalando dependencias..."
sudo yum update -y
sudo yum install -y docker git unzip curl

echo "🐳 [2/6] Iniciando Docker..."
sudo service docker start
sudo usermod -aG docker ec2-user

echo "🧰 [3/6] Instalando Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
     -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

echo "🌐 [4/6] Creando red Docker 'campus_net'..."
docker network create campus_net || echo "Red ya existente"

echo "🚀 [5/6] Levantando microservicios..."
docker-compose -f users/docker-compose.yml up -d
docker-compose -f enrollment/docker-compose.yml up -d
docker-compose -f union/docker-compose.yml up -d
docker-compose -f history/docker-compose.yml up -d
docker-compose -f 18.ai-recommender-service/docker-compose.yml up -d

echo "✅ [6/6] Despliegue completado."
docker ps
