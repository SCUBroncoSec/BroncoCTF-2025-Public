FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install flask PyJWT
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 80