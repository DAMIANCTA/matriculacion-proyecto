FROM golang:1.20-alpine
WORKDIR /app
COPY . .
RUN go mod init subjectsearch && go get github.com/gofiber/fiber/v2 && go get github.com/lib/pq && go build -o app .
EXPOSE 3009
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3007"]
