# Python for MegaPi version (0.1.9)
First repository --  (Time stamp 3:11 PM  1/10/2019)
# and the Raspberry Pi 3
## How To Use
### Prepare the Arduino IDE
 * Download the Arduino library for Makeblock
 https://github.com/Makeblock-official/Makeblock-Libraries/archive/master.zip
 * Copy the makeblock folder to your arduino default library. Your Arduino library folder should now look like this 
   * (on Windows): ```[x:\Users\XXX\Documents]\Arduino\libraries\makeblock\src```
   * (on Mac OSX): ```[\Users\XXX\Documents]\Arduino\libraries\makeblock\src```
 * Open Arduino IDE, choose the firmware from <em>File&gt;Examples</em>.
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/firmware.jpg)
 * Compile and upload firmware for your Raspberry Pi 3

### Prepare the Raspberry Pi 3
 * On your Raspberry Pi, disable the login prompt from Desktop->Menu->Preferences->Raspberry Pi Configuration.


![image](https://user-images.githubusercontent.com/23004042/50984814-598df100-14c8-11e9-8689-bddfefe25571.png)

Disable the Raspberry Pi 3 bluetooth and restore UART0 **(/dev/ttyAMA0)** over GPIOs 14&15


* Disable the Raspberry Pi 3 bluetooth . . .

1. Search `pi3-disable-bt` in file `/boot/overlays/README`, it will show you, how to disable the bluetooth, if you want switch the bluetooth to mini-UART(ttyS0), you can search `pi3-miniuart-bt` 

![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/pi3-disable-bt.jpg)

2. Modify the file `/boot/config.txt`, At the end of the file, add the following content
```
#Enable uart
enable_uart=1
dtoverlay=pi3-disable-bt
```

![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/configTxt.jpg)

3. reboot the raspberry pi

4. open the Terminal and input the command `sudo systemctl disable hciuart`

5. Now you can use **/dev/ttyAMA0** as UART over GPIOs 14&15 


 * install python library for Makeblock
 ```
 sudo pip install megapi
 ```
 Inter Python2
 **$ idle**
 
 * the initial code for python.
```
 from megapi import *
 bot = MegaPi()
 bot.start()
 ```
 * python your code

### Wiring
* Using MegaPi
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/megapi.jpg)

## Python API
 * Start
 	* **MegaPi**()
 	* **start**()
 	
 * GPIO
 	* **digitalWrite**( pin, level )
 	* **pwmWrite**( pin, pwm )
 	* **digitalRead**( pin, **def** onResult )
 	* **analogRead**( pin, **def** onResult )
 	
 * Motion
	* DC Motor
	  * **motorRun**( port, speed )
	  * **motorMove**( leftspeed, rightspeed )
	* Servo Motor
	  * **servoRun**( port, slot, angle )
	* Encoder Motor
	  * **encoderMotorRun**( port, speed )
	  * **encoderMotorMove**( port, speed, distance, **def** onFinish )
	  * **encoderMotorMoveTo**( port, speed, position, **def** onFinish )
	  * **encoderMotorSetCurPosZero**( slot )
	  * **encoderMotorPosition**( slot, **def** onResult)
	  * **encoderMotorSpeed**( slot, **def** onResult)
	* Stepper Motor
	  * **stepperMotorRun**( port, speed )
	  * **stepperMotorMove**( port, speed, distance, **def** onFinish )
	  * **stepperMotorMoveTo**( port, speed, position, **def** onFinish )
	  
 * Sensors
 	* Ultrasonic Sensor
 	  * **ultrasonicSensorRead** ( port, **def** onResult ) 
 	* LineFollow Sensor
 	  * **lineFollowerRead** ( port, **def** onResult ) 
 	* Light Sensor
 	  * **lightSensorRead** ( port, **def** onResult ) 
 	* Sound Sensor
 	  * **soundSensorRead** ( port, **def** onResult ) 
 	* Temperature Sensor
 	  * **temperatureRead** ( port, **def** onResult ) 
 	* PIR Motion Sensor
 	  * **pirMotionSensorRead** ( port, **def** onResult ) 
 	* Touch Sensor
 	  * **touchSensorRead** ( port, **def** onResult ) 
 	* LimitSwitch
 	  * **limitSwitchRead** ( port, slot, **def** onResult ) 
 	* Humiture Sensor
 	  * **humitureSensorRead** ( port, type, **def** onResult ) 
 	* Gas Sensor
 	  * **gasSensorRead** ( port, **def** onResult )
 	* Flame Sensor
 	  * **flameSensorRead** ( port, **def** onResult ) 
 	* Button
 	  * **buttonRead** ( port, **def** onResult ) 
 	* Potentiometer
 	  * **potentiometerRead** ( port, **def** onResult )
 	* Joystick
 	  * **joystickRead** ( port, axis, **def** onResult )
 	* 3-Axis Accelerometer and Gyro Sensor
 	  * **gyroRead** ( port，axis, **def** onResult )
 	* Compass
 	  * **compassRead** ( **def** onResult )
 	* Pressure Sensor for BMP085 and BMP180
 	  * **pressureSensorBegin** ( ) 
 	  * **pressureSensorRead** ( type, **def** onResult ) #1:Pressure #2:Temperature #3:Altitude #4:Real altitude #5:Sealevel Pressure
 	
 * Display
 	* RGB Led
 	  * **rgbLedSetColor** ( port, slot, index, r, g, b )
 	  * **rgbLedShow** ( port, slot )
 	  * **rgbLedDisplay** ( port, slot, index, r, g, b )
 	* 7-segment Display
 	  * **sevenSegmentDisplay** ( port, value )
 	* Led Matrix Display
 	  * **ledMatrixDisplayMessage** ( port, x, y, msg )
 	  * **ledMatrixDisplayRaw** ( port, buffer )
 	* Serial LCD Display
 	  * **lcdDisplay** ( string )
 	  
 * Others
 	* DSLR Shutter
	  * **shutterOn** ( port )
	  * **shutterOff** ( port )
	  * **focusOn** ( port )
	  * **focusOff** ( port )

###Latest versions of the software are (1/10/2019)
MegaPi2560 firmware	0e.01.016
Arduino IDE	1.8.8
MegaPi library for the Arduino IDE	3.2.6
Python library for the Raspberry	0.1.9

###Learn more from Makeblock official website: www.makeblock.com
