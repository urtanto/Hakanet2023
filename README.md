# Docker guid

### Start guid

1. Download needed image
   ```bash
   docker pull python:3.10
   ```
2. Build your image
   ```bash
   docker build . --tag main
   ```
3. Run you image
   ```bash
   docker run -p 8000:8000 -d main
   ```
4. Stop you container
   ```bash
   docker stop CONTAINER_ID
   ```
5. Start you container
   ```bash
   docker start CONTAINER_ID
   ```
6. Logs of container
   ```bash
   docker logs CONTAINER_ID
   ```

### Tips and Tricks

1. To show all images
    ```bash
       docker images
    ```
2. To show all containers
    ```bash
       docker ps
    ```
3. To show all containers (finished)
    ```bash
       docker ps -a
    ```
4. To delete image
    ```bash
       docker rmi IMAGE_ID(or image tag)
    ```
5. To delete container
    ```bash
       docker rm CONTAINER_ID
    ```
6. Log in container
    ```bash
       docker exec -it CONTAINER_ID
    ```
