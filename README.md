# ObstructionDetectionVehicle-ODV-

An IoT based project that demonstrates a vehicle that stops before collision. The vehicle is created using a Raspberry Pi and the collision is detected using a HC-SR04 ultraSonic sensor. The vehicle is controlled using an App "Bluetooth Terminal HC05" and it communicates with a HC05 sensor which in turn communicates with the Raspberry Pi.

## Prerequisites
* Raspberry Pi 3
* HC05 bluetooth sensor
* L293D Motor Driver
* HC-SR04 ultrasonic sensor
* Basic Python and Command-line knowledge

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the follwing dependencies
```bash
sudo pip install wiringpi
sudo pip install RPi.GPIO
sudo pip install pyserial
```

## Usage
To receive serial input from HC05 Sensor, you will need to configure your Raspberry Pi. You can find all the steps in this video: https://www.youtube.com/watch?v=PT2ryjQl3Ns  
These steps will disable your bluetooth adapter for file transfer but will allow serial input which can be used with a lot of IoT devices like Arduino, Esp8266,etc.

### step-1
In the terminal type,
```bash
sudo vim /boot/config.txt
```
* Press i to insert text
* go to the last line and type 'enable_uart=1'
* exit vim by pressing [ESC] button and then typing :wq
* in the terminal type 
```bash
sudo reboot
```
Reboot saves the changes

### step-2
In the terminal type,
```bash
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
```

### step-3
In terminal type,
```bash
sudo vim /boot/cmdline.txt
```
* Press i to insert text
* remove the words 'console=serial0,115200'
* exit vim by pressing [ESC] button and then typing :wq

### step-4
In the terminal type,
```bash
sudo vim /boot/config.txt
```
* Press i to insert text
* go to the last line and type 'dtoverlay=pi3-miniuart-bt'
* exit vim by pressing [ESC] button and then typing :wq
```bash
sudo reboot
```

To create the launcher script for the Raspberry Pi follow the instructions in the link: https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/

## Pictures
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220236.jpg)
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220305.jpg)
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220316.jpg)
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220324.jpg)
