# Spotlight API

Add checkpoint to `model/checkpoints/night2day/`

```
docker build -t spotlight .
docker run -d -p 5000:5000 spotlight

# to stop the container
docker stop <container_id>
```

Test the API on `http://0.0.0.0:5000/spotlight/api/v1.0/`
