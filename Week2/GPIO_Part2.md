# Raspberry Pi GPIO-Part 2: Adafruit DC Motor HAT for Raspberry Pi

## Overview

 The **DC+Stepper Motor HAT from Adafruit** is a perfect add-on for any motor project as it can drive up to 4 DC or 2 Stepper motors with full PWM speed control. However, the Raspberry Pi does not have a lot of PWM pins, we use a fully-dedicated PWM driver chip onboard to both control motor direction and speed. This chip handles all the motor and speed controls over 12C. Only two GPIO pins (SDA & SCL) are required to drive the multiple motors, and since it is 12C you can also connect any other 12C devices or HATs to the same pins.

##### Features:

 * 4 H-Bridges: TB6612 MOSFET chipset provides 1.2A per bridge (3A brief peak) with thermal shutdown protection, internal kickback protection diodes. Can run motors on 4.5VDC to 13.5VDC.
 * **Up to 4 bi-directional DC motors** with individual 8-bit speed selection (so, about 0.5% resolution).
 * **Up to 2 stepper motors** (unipolar or bipolar) with single coil, double coil, interleaved or micro-stepping.
 * Big terminal block connectors to easily hook up wires (18-26AWG) and power.
 * Polarity protected 2-pin terminal block and jumper to connect external 5-12VDC power.
 * Install the easy-to-use Python library.

## Assembly

 **The Motor HAT** comes with an assembled and tested HAT, terminal blocks, and 2x20 plain header. Some soldering is required to assemble the headers on. Here we leave a link with a [step-by-step](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/assembly) guide of how to solder the headers and a video to show you [tips on soldering](
 https://www.youtube.com/watch?v=QKbJxytERvg).

 <img src="raspberry_pi_2348_top_ORIG.jpg" alt="rpi" style="width: 400px;"/>

Once the motor HAT is assembled, we place it on top so that the short pins of the 2x20 header line up with the pads on the HAT.

 <img src="raspberry_pi_place.jpg" alt="rpi-hat" style="width: 400px;"/>

## Powering Motors

Note the HAT does not power the Raspberry Pi, and we strongly recommend having two separate power supplies - one for the RPi and one for the motors, as motors can put a lot of noise onto a power supply and it could cause stability problems.

##### Voltage requirements

The motor controllers on this HAT are designed to run from **5V to 12V**. Therefore, the first important thing is to verify the voltage specifications for the motor. Some small hobby motors are only intended to run at 1.5V (**MOST 1.5-3V MOTORS WILL NOT WORK or will be damaged by 5V power**), but its just as common to have 6-12V motors.

##### Current requirements

The motor driver chips that come with the kit are designed to provide up to **1.2 A per motor**, with 3A peak current. Note that once you head towards 2A you will probably want to put a heat-sink on the motor driver, otherwise you will get thermal failure, possibly burning out the chip.

**Am important thing you can not run motors off of a 9V battery so don't waste your time/batteries!**

Therefore, you can use a 9V 1A, 12V 1A, or 12V 5A DC regulated switching power adapter. In case you want to make it portable, you can use a big Lead Acid or multiple-AA NiMH battery pack of 4 to 8 batteries to vary the voltage from about 6V to 12V as your motors require.

<img src="raspberry_pi_powerplug.jpg" alt="hat-power" style="width: 400px;"/>
