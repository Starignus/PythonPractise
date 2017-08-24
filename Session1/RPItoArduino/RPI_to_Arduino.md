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






