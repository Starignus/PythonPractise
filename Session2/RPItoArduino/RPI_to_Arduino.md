# Setting up Arduino on your headless Raspberry Pi

### In case you are wondering why...
RPi and Arduino are complementary platforms and one doesn't exclude the other. If you combine their capabilities you can achieve amazing results. But why?
    * The community! Arduino has a lot of materials readily available online, from libraries, to examples. If you have something in mind probabily someone has already done it and shared the documentation.
    * You might have a project that is already working on Arduino, but you might need just a bit more processing power, so the Raspberry can come to the rescue.
    * The RPi doesn't go well with 5V logic levels, it only operates with 3.3V and its pins do not accomodate 5V.
    * If you fry an Arduino you can replace the damaged microcontroller chip easily for less than £10. That gives you the freedom to experiment a bit more, without damaging the RPi.
    * Raspbian operating system doesn't have real-time control capabilities, whereas a microcontroller like Arduino can handle those operations.


### Installing Arduino
From the terminal of your computer connected to the RPi via ssh type:
```bash
sudo apt-get install arduino
```
It is going to ask you to agree on using additional disk space, type Y and press Enter.

Once we have done this installation we need to grant ourselves the permission to use the serial port. In order to do so we are going to add our user (pi) to the _tty_ and _dialout_ groups with two commands:
```bash
sudo usermod -a -G tty pi
```
```bash
sudo usermod -a -G dialout pi
```

### Working with the Arduino IDE

If you now connect a keyboard, mouse and screen to your RPi, you can see that in the menu under the "Electronics" section the Arduino IDE has been installed. If you are familiar with the Arduino IDE, you can go ahead and use the Arduino IDE as you would on your laptop. The only difference is that the RPI is a slower to compile the new lines of code from the RPi with respect to a laptop.
To test if Arduino IDE is working you can connect the Arduino to the RPi using one of the available USB ports like so:

<img src="img/connected-boards.png" alt="arduino" style="width: 400px;"/>

Then run the Arduino IDE.

<img src="img/arduino-ide.png" alt="arduino" style="width: 400px;"/>

Click **Tools->Serial Port** and select the USB serial port to which your Arduino is connected (usually /dev/ttyACM0). Then, click **Tools->Board->Arduino Uno**. Then you can open the basic sketch "Blink" by clicking on **File->Example->01. Basics-> Blink. You can then upload the sketch on the Arduino by clicking the "Upload" button (the one with an arrow).

<img src="img/arduino-blink.png" alt="arduino" style="width: 400px;"/>

Once uploaded you will see the LED on pin 13 blink.

**Note:** If /dev/ttyACM0 doesn't work, you can find out in which serial port your Arduino is plugged by unpluggin it from the RPi. Then on the Rpi terminal type:

```bash
ls /dev/tty*
```

This command lists all the connected devices, it should show "/dev/ttyAMA0". Then plug in your Arduino again and enter the same command and you should find the right port popping up.

<img src="img/arduino-not-on-ttylist.png" alt="arduino" style="width: 400px;"/>

<img src="img/arduino-on-ttylist.png" alt="arduino" style="width: 400px;"/>
