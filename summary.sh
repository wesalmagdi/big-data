#!/bin/bash
IMAGE_NAME="cosmetics-analytics:latest"
CONTAINER_NAME="analytics_container"
HOST_RESULTS="./results"
DATA_FILE="data.zip"


echo "Building Docker image..."
docker build -t $IMAGE_NAME .

mkdir -p $HOST_RESULTS

docker run --name $CONTAINER_NAME python ingest.py $DATA_FILE

echo "Copying output files from container..."

# docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv $HOST_RESULTS/
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv $HOST_RESULTS/
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt $HOST_RESULTS/
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt $HOST_RESULTS/
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt $HOST_RESULTS/
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png $HOST_RESULTS/
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt $HOST_RESULTS/

echo "Files copied successfully."

echo "Stopping container..."
docker stop $CONTAINER_NAME

echo "Removing container..."
docker rm $CONTAINER_NAME

echo "Done."