#using python runtime as the base image 
FROM python:3.9-slim

#setting up the working directory 
WORKDIR /app

#copy the current contents to working directory 
COPY . /app

#install the dependencies 
RUN pip install --no-cache-dir -r requirements.txt

#command to run the scripts 
CMD ["python", "data_cleaning.py"]
