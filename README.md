# Hitungin
Hitungin is a camera based people counting system using OpenCV Framework. This project is aimed to create a robust counting system to generate the mapping crowd in some building.

# System Used
- Ubuntu 18.04
- OpenCV3 Python
- Flask Framework

## Installation

Hitungin consists of 2 dependecies framework :
- OpenCV3 Python
Install the OpenCV Python following [this tutorial](https://www.learnopencv.com/install-opencv-4-on-ubuntu-18-04/).
- Flask
Install flask using pip with this command after entering your python virtual environment.
    ```sh
    $ pip install flask
    ```
After installing the dependecies you can start to use the project

First you must clone the project to your system
```sh
$ git clone https://github.com/oracl4/hitungin.git
```

After cloning the project you can start running the project using runScript.sh in hitungin workspace

```sh
hitungin$ ./runScript.sh
```
## Development

### Counter Framework
- You can change the video source and destination for the project with changing the input tags on src/counter/runScript.sh like this
    ```sh
    python src/counter/people_counter.py
    --prototxt src/counter/mobilenet_ssd/MobileNetSSD_deploy.prototxt \
    --model src/counter/mobilenet_ssd/MobileNetSSD_deploy.caffemodel \
    --input input/nameoftheinputfile.mp4 \
    --output output/nameoftheoutputfile.avi
    ```
- The default configuration is using webcam and no output file
### Streamer Configuration
- You can also change the source of video stream in flask app with another input file that "renamed" into input.mp4 that placed on input folder
- The default configuration is also using webcam

### After Running > Website Integration
- Change the source ip and port on website HTML with the local ip address and port in flask
- Change the database PHP configuration in people_counter.py and uncomment it

### Reference
- https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
- https://blog.miguelgrinberg.com/post/video-streaming-with-flask
