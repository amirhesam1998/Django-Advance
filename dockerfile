FROM python:3.11   
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./core /app
CMD [ "python" , "manage.py" , "runserver" , "0.0.0.0:8000" ]



# Dockerfiles:
# Save the changes in the 'app' folder in the image docker
# Copy the 'requirements.txt' file to the 'app' image folder that I created
# Copy the code I wrote from the 'core' folder to the 'app'  image folder


# COMMAND:
# docker build -t django .                                    Build what we built (.) with Django tag
# docker images                                               show images folders
# docker run -p 8000:8000 django                              Run the django image I made with port 8000
# docker ps -a                                                show runing containers
# docker rmi fb                                               delete fb image