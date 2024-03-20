# VertexAi Gemini
Inspire 에서 사용할 vertext ai 
cloud run에 서비스하고 
Golang 서버 Inspire 에서 요청을 받아서 생성형 AI 모델을 사용해서 텍스트 생성

python fast api

```
docker build -t test:latest .
docker run -it -p8888:80 test:latest
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

### deploy
```
gcloud builds submit . --tag=asia-northeast3-docker.pkg.dev/{Project_id}/{projectname}/{imagename}:1.0.5

```
