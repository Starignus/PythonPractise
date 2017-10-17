# Alternatives/Comparison between Arudino and Raspberry PI

### Why Arduino?

RPi and Arduino are complementary platforms and one doesn't exclude the other. If you combine their capabilities you can achieve amazing results. But why?
  * The community! Arduino has a lot of materials readily available online, from libraries, to examples. If you have something in mind probably someone has already done it and shared the documentation.
  * You might have a project that is already working on Arduino, but you might need just a bit more processing power, so the Raspberry can come to the rescue.
  * The RPi doesn't go well with 5V logic levels, it only operates with 3.3V and its pins do not accommodate 5V.
  * If you fry an Arduino you can replace the damaged microcontroller chip easily for less than £10. That gives you the freedom to experiment a bit more, without damaging the RPi.
  * Raspbian operating system doesn't have real-time control capabilities, whereas a microcontroller like Arduino can handle those operations.
  * Arduino is very easy to start up

### Why Raspberry PI?

The Raspberry Pi definitely performs best when there are heavy calculations into play but also is great for:
* Internet or network connectivity projects (IoT)
* Graphical applications
* The need for USB peripherals such as a web cam
* Big Data projects
* ... and many more applications!

To chose between the two there's is this [Make:zine article](http://makezine.com/2015/12/04/admittedly-simplistic-guide-raspberry-pi-vs-arduino/) that can help you out.

### What are some alternatives to Raspberry Pi for the IoT?
- [Arduino Yun](https://store.arduino.cc/arduino-yun) it is an Arduino with WiFi connection capabilities ideal for Iot
- [Intel IoT Developer Kit](https://software.intel.com/en-us/iot/hardware/dev-kit)
- [Photon](https://store.particle.io/) very tiny Wifi enabled board
- [Beaglebone](http://beagleboard.org/bone) it is a Raspberry Pi competitor with some analog pins functionality
- [ESP8266](http://espressif.com/en/products/hardware/esp8266ex/overview)

### What are some alternative micro-controllers to Arduino?
- [ARM mBed](https://os.mbed.com/platforms/mbed-LPC1768/)
- [STM32](http://www.st.com/en/microcontrollers/stm32-32-bit-arm-cortex-mcus.html)
- [Teensy](https://www.pjrc.com/teensy/)
- [pyboard](https://store.micropython.org/#/store) runs microPython (comparison and guide with microPython vs. Arduino)
