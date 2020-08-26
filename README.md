# ObstructionDetectionVehicle-ODV-

An IoT based project that demonstrates a vehicle that stops before collision. The vehicle is created using a Raspberry Pi and the collision is detected using a HC-SR04 ultraSonic sensor. The vehicle is controlled using an App "Bluetooth Terminal HC05" and it communicates with a HC05 sensor which in turn communicates with the Raspberry Pi.

## Prerequisites
* Raspberry Pi 3
* HC05 bluetooth module
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

You will need to install Bluetooth Terminal HC-05 app for android(not sure for iOS) and you will need to pair your smartphone device and the HC-05 sensor.  
* To move forward you will need to type a  
* To move backward you will need to type b  
* To move left you will need to type c  
* To move right you will need to type d  
* To stop you will need to type e  

## Detailed Connections
Pinout diagram of Raspberry Pi GPIO  
![Image of GPIO](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/Screenshot%20from%202020-08-26%2012-58-03.png)  

### For the motor Driver L293D
* connect I1 to GPIO2(3)
* connect I2 to GPIO3(5)
* connect I3 to GPIO4(7)
* connect I4 to GPIO17(11)

### For HC-05 bluetooth module
* connect 5V(4) to vcc
* connect GND(6) to GND
* connect GPIO14(8) to RXD (GPIO14 - TXD pin of Raspberry Pi)
* connect GPIO15(10) to TXD (GPIO15 - RXD pin of Raspberry Pi)

### For HC-SR04 ultrasonic Sensor
* connect GPIO27(13) to Trig of HC-SR04
* connect GPIO22(15) to Echo of HC-SR04
* connect 3v3(17) to Vcc of HC-SR04
* connect GND(20) to GND of HC-SR04

Connect the motors to the M1,M2,M3 and M4 pins in the motor Driver and give the motor driver 12V of supply.
Provide an external power supply to Raspberry Pi(in my project i am providing the supply through a Power bank).  

## Pictures
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220236.jpg)
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220305.jpg)
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220316.jpg)
![Image of ODV](https://github.com/AtulKUchil/ObstructionDetectionVehicle-ODV-/blob/master/images/IMG_20200825_220324.jpg)
