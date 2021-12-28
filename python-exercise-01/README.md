make image
 docker-compose build --no-cache

make and run container
 docker run --rm <image-local-repository:tag> python -c "from calculator import calculator; print (calculator( 12, 10, '+'))"


