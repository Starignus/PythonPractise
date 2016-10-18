# Raspberry Pi GPIO-Part 2: Adafruit DC Motor HAT for Raspberry Pi

## Overview

 The **DC+Stepper Motor HAT from Adafruit** is a perfect add-on for any motor project as it can drive up to 4 DC or 2 Stepper motors with full PWM speed control. However, the Raspberry Pi does not have a lot of PWM pins, we use a fully-dedicated PWM driver chip onboard to both control motor direction and speed. This chip handles all the motor and speed controls over 12C. Only two GPIO pins (SDA & SCL) are required to drive the multiple motors, and since it is 12C you can also connect any other 12C devices or HATs to the same pins.

 **The Motor HAT** comes with an assembled & tested HAT, terminal blocks, and 2x20 plain header. Some soldering is required to assemble the headers on. Here we leave a link with a step-by-step guide of how to solder the headers and a video to show you
 
 <img src="raspberry_pi_2348_top_ORIG.jpg" alt="rpi" style="width: 400px;"/>

###### Features:
* 4 H-Bridges: TB6612 MOSFET chipset provides 1.2A per bridge (3A brief peak) with thermal shutdown protection, internal kickback protection diodes. Can run motors on 4.5VDC to 13.5VDC.
* **Up to 4 bi-directional DC motors** with individual 8-bit speed selection (so, about 0.5% resolution).
* **Up to 2 stepper motors** (unipolar or bipolar) with single coil, double coil, interleaved or micro-stepping.
* Big terminal block connectors to easily hook up wires (18-26AWG) and power.
* Polarity protected 2-pin terminal block and jumper to connect external 5-12VDC power.
* Install the easy-to-use Python library.
