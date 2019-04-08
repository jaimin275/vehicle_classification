# Vehicle Classification
Car and Bike classification project using Convolutional Neural Network

## Prerequisites
* Basic Machine Learning Knowledge
* Lesson 1 and Lesson 2 from fastai deep learning 2019 course
* Basic Python

## What I have used
* windows
* Google Colab (For faster training of ML model)
* fastai library
* python
* jupyter notebook


#### My project Structure
![alt text](https://github.com/jaimin275/vehicle_classification/blob/master/Document/images/project_structure.jpg)


## Start
Follow lesson 1 and lesson 2 from fastai depp learning 2019 course from [here](https://course.fast.ai/).
Download this repository and open vehical_classification.ipynb file in google colab

[Follow this steps to configure colab](https://course.fast.ai/start_colab.html)

first you need to set your storage. In my case i used google drive which is set in first line of code in notebook.

after setting storage run all cell one by one and understand what's going on.

while downloading dataset from browser after pasting javascript code in browser console, if download popup is not start check you have any popup blocker running in your browser. If you are running popup blocker then disable and run javascript code again.(In my case i disabled adblock plus extension)

then continue until you create imageDataBunch as lesson 2 lecture show.
train your model and save stage-1 and stage-2.

Now you have to clean some images while cleaning if ImageCleaner() running infinitely then follow below steps to clean images.
1. copy your project into local computer
2. install required fastai library by following [this](https://docs.fast.ai/install.html) article. (In my case i am using two conda command for install fastai)
3. run notebook in local jupyter and run cells until you create learn object.(do not train model because you already have two train model stage-1 and stage-2 from colab).
4. skip until cleaning up section and run cleaning up section cells to clean image dataset.
5. upload that dataset to drive.
6. run all the cells in colab.
7. if you get an error while creating ImageDataBunch.from_csv ([Errno 2] No such file or directory: '/content/gdrive/My Drive/ML-Project/vehicle-classification/data/bike\\00000000.jpg') then try creating ImageDataBunch.from_folder().
8. now train your model and save stage-1 and stage-2
9. Now time to put your model in production

## Production
Please refer production section of [this](https://course.fast.ai/) article if you want to run your model in cloud.
and also [this](https://medium.com/@pierre_guillou/deep-learning-web-app-by-fastai-v1-3ab4c20b7cac) article for more info.

I am running this model locally.

1. Go to [https://github.com/render-examples/fastai-v3](https://github.com/render-examples/fastai-v3) and download the file fastai-v3-master.zip from this directory by clicking on the green button “Clone or Download” (or make a git clone on your terminal) .
2. Extract the zip on your test space. For example, into file:///C:/vehicle_classification/production/
3. In your terminal, install via pip the necessary libraries to have a local Starlette server:
* pip install Starlette
* pip install aiofiles
* pip install uvicorn
* pip install aiohttp
* pip install python-multipart

4. run your server.py file "python app/server.py serve"
* If you don't get any error you will see your localhost running in terminal after some time. 
* If you getting any error while running this code then follow below steps
1. copy export.pkl file from drive and paste it in app/models/
2. replace server.py file with this repository server.py file
3. run server.py file by "python app/server.py serve" in terminal. you can see your localhost is running.
4. open localhost and browse any test_image then click analyse and see result.
5. Done.


Note: This repository code is currently running. If you have any problem with your code, compare your code with this repo code and find the difference.




