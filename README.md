# Clearing Blind spots Using Ultrasonic sound sensors

![image](https://github.com/charansingh25/clearing-blind-spots/assets/104901834/d2c0d5e7-b1c4-42f7-bc7a-cc9c59c76218)

## Objetive and summary
* An Iot and sensors based project in which we developed a cost-effective solution to assist vehicle drivers in clearing blind
spots and preventing accidents.
* We also implemented Ultrasonic sensors to accurately detect and track the location and
speed of nearby vehicles in real-time
* Utilized Tkinter to dynamically visualize nearby vehicles, changing colors based
on proximity forimproved driver awarenes

## TinkerCAD

Check out the tinkercad model of the connections - [TinkerCAD](https://www.tinkercad.com/things/desTyeIwnWf-serial-communication-attempt/editel?sharecode=NzNrlqZZhKk1uK5iBHZDVh_5k9bap95PaLXEoZBweaU)


![image](https://github.com/charansingh25/clearing-blind-spots/assets/104901834/9d250293-75d2-4984-8d7d-044e8d80dd63)


## Arduino 

* Intergrated 4 ultrasonic sound sensors to ARDUINO board to detect and get the details of nearby moving objects
* Data from the sensors is analyzed in the Arduino IDE to calculate the distances of the objects. COM port 4 is used for this communication. The serial plotter feature in the arduino IDE can be used to ensure that the sensors are working properly.

## Tkinter 

* On the GUI, 4 dots representing the obstacles’ distances from the vehicle are programmed. If an object is far from the vehicle then the dot is of Green color, when it is at an intermediate distance the color is yellow and when the object or a nearby vehicle dangerously close to the vehicle then the dot is red

## Working 

Each sensor has 4 pins, Trig, Echo, Vcc and GND. Trig pin corresponds to the transmitter which transmits the ultrasonic pulse . Echo pin corresponds to the Receiver, which receives the reﬂected ultrasonic wave. The Time delay between the transmission and receiving of the pulse depends on the distance between the sensor and the obstacles. The Vcc pin of all 4 sensors is connected to the 5v supply on the arduino chip using the breadboard. Similarly, the GND pin of each sensor is connected to the ground of the arduino. The other two pins are connected to any two of the 13 Digital I/O pins on the microprocessor


