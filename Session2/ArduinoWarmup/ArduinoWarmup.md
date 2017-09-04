# What is Arduino?

<img src="arduino-environment.png" alt="arduino-environment" style="width: 400px;"/>

### What is Arduino: Hardware
An Arduino is essentially a microcontroller. That is a small "computer" (SoC - System on a Chip) on a single integrated
circuit containing a processor core, memory and programmable input/output peripherals (a.k.a. sensors and actuators).

#### Physical structure of arduino board

<img src="board_anatomy.png" alt="arduino-anatomy" style="width: 400px;"/>

1. Digital pins Use these pins with digitalRead(), digitalWrite(), and analogWrite(). analogWrite() works only on the pins with the PWM symbol.
2. Pin 13 LED The only actuator built-in to your board. Besides being a handy target for your first blink sketch, this LED is very useful for debugging.
3. Power LED Indicates that your Arduino is receiving power. Useful for debugging.
4. ATmega microcontroller The heart of your board.
5. Analog in Use these pins with analogRead().
6. GND and 5V pins Use these pins to provide +5V power and ground to your circuits.
7. Power connector This is how you power your Arduino when it’s not plugged into a USB port for power. Can accept voltages between 7-12V.
8. TX and RX LEDs These LEDs indicate communication between your Arduino and your computer. Expect them to flicker rapidly during sketch upload as well as during serial communication. Useful for debugging.
9. USB port Used for powering your Arduino Uno, uploading your sketches to your Arduino, and for communicating with your Arduino sketch (via Serial. println() etc.).
10. Reset button Resets the ATmega microcontroller.

#### Digital / Analog pins
https://www.arduino.cc/en/Tutorial/DigitalPins

#### PWM
https://www.arduino.cc/en/Tutorial/PWM

### What is Arduino: Software

#### Quick tour of the Arduino IDE

Arduino has it's own integrated development environment that simplifies some of the operations. The IDE manages library, offers a built-in compiler and has a lot of examples and references.

<img src="arduino_ide.png" alt="arduino-ide" style="width: 400px;"/>

1. Verify: Compiles and approves your code. It will catch
errors in syntax (like missing semi-colons or parenthesis).
2. Upload: Sends your code to the Uno. When you click it, you
should see the lights on your board blink rapidly.
3. New: This buttons opens up a new code window tab.
4. Open: This button will let you open up an existing sketch.
5. Save: This saves the currently active sketch.
6. Serial Monitor: This will open a window that displays any
serial information your Uno Board is transmitting. It is very
useful for debugging.
7. Sketch Name: This shows the name of the sketch you are
currently working on.
8. Code Area: This is the area where you compose the code
for your sketch.
9. Message Area: This is where the IDE tells you if there were
any errors in your code.
10. Text Console: The text console shows complete error
messages. When debugging, the text console is very useful.
11. Board and Serial Port: Shows you what board and the
serial port selections

#### Anatomy of A Sketch

#### Arduino Language
https://www.arduino.cc/en/Tutorial/Variables
https://www.arduino.cc/en/Reference/FunctionDeclaration
https://www.arduino.cc/en/Reference/HomePage
