# image_to_text
In this project we are extracting the text out of the image and successfully showing that text on our web page. We simply take image of a vehicle as input and after processing that image we are extracting text out of it.

# Process of gathering data.
When we start making this project we have checked many online resources available for this task and then we come to know  that there exist a dataset in opencv library of python.
So we use that data available in the file "haarcascade_russian_plate_number.xml". We have downloaded this file from github itself.

# Working
Firstly we take image of vehicle as input. Then our model will detect the number plate on the vehicle. After detection it will crop the detected area out of that image. After that we will convert that cropped image into gray scale. Then we will increase the contrast of the image and after that we will pass that image to pyteeseract so that it can extract text out of it. After getting that text we will display it on the web page.

# Steps for running the web server on local machine

1. Install the required packages(You can get it from requirement.text file).
2. Install pyteeseract from this link(tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe)(WINDOWS) and also using pip install pytesseract(BOTH ARE MANDATORY).
3. Download the github repository.
4. Run the server using app.js and then open index.html.
5. Now You are ready to use our app!! 

# Error in deployment on heroku
We have tried a lot for deploying our app to heroku but due to pyteeseract we are not able to deploy it.
