# Python GUI with PyQt5

![pyqt_img](https://user-images.githubusercontent.com/56091634/93661741-d92eda00-fa77-11ea-9b50-acb4f85264d9.jpg)

## INTRODUCTION

The metropolitan road system is one of the most important infrastructures and also one of the most important compositions of urban livelihood. Every year, the drainage system fails to control the problems generated from water and generates huge problems in the city and broadly affects the system. The road system in many cities suffers from various problems related to water, like road waterlogging, raising drainage load resulted from concentrated run-off, wastage of rainwater resources due to falling in replenishing of the surface runoff to the groundwater system at the time of heavy rainstorm period. The road waterlogging also affects its traffic system, even result in temporal regional traffic locking, and degrades the quality and service life of the road works. The road surface runoff contaminates and harms the surrounding environment, and under the disturbance of vehicle wheels, the dust accumulated on the road pollutes urban air in a dry situation.[1]
An analysis showed that water-related problems have mainly resulted from manmade factors such as low design standards of the road drainage system, poor environmental protection facilities for rainwater storage and infiltration, high-raised green belt, and therefore the weakness of road building technology. Countermeasures were proposed, like raising road drainage standards, innovating and popularizing road building materials and technology, and lowering the elevation of the green belts. A case study showed that the application of the previous asphalt concrete as paving material and the adoption of lowering green belts could significantly ease the street waterlogging, reduce the runoff pollution, urban drainage load, and improve the rain resources utilization. Underpasses, where quickly accumulating water can cause seriously dangerous situations for passing vehicles, are among the most vulnerable infrastructures in case of intense rain, which are becoming more and more frequent due to climate change. The monitoring and alarm systems we offer aim to timely warn of flooding of the underpass and consequently to stop passage by activating the relevant signs (variable message panels, traffic lights, etc.). The traffic is stopped automatically, without needing to pass through a central control center, when the hydrometric thresholds set by the authorities are exceeded. The risk of false alarms is minimized by the contemporaneous presence of several sensors and a webcam for visual monitoring. Systems are ready to be interfaced with operating machines, such as electric pumps; to monitor their operation and proper disposal of surface water. The complete monitoring of the status of the current situation can be easily seen on a Graphical User Interface (GUI) system.[2]


 
## PROBLEM DEFINITION

## PROJECT OBJECTIVE
This project is based on underpass waterlogging problems caused in the metropolitan cities and urban areas. The road systems in many cities are suffering from various water-related problems, such as road water logging, increased drainage load, waste of rainwater resources, etc. Also, heavy rain induces more severe problems and result in loss of lives. To overcome this scenario: an automated water removal method is used to reduce waterlogging, an alert system will indicate any risk, a camera will depict any motion caused due to accidents and the weather-responsive management strategies will lower the pollution caused by the traffic. The same water after being filtered is utilized for domestic purposes or stored for future use.
To accomplish this task, project is divided into following steps:
•	Development of water level indicator, alert system and anti-waterlogging solution with the help of water level indicator, buzzer, LCD screen and pump.
•	Development of GUI to broadcast all the readings and live feed directly to the authorities who are responsible to take the actions.
•	Development of a motion detector with the help of the PIR sensor and deployment of automatic light glower and smoke detector with the help of LDR and smoke sensor.
•	Construction of water conservation plant to conserve the water pumped out from underpass.
•	Interfacing all of the above developed parts in one for finalizing the project.


#### 1.	MQ2 Sensor:
MQ2 is one among the commonly used gas sensors in the MQ sensor series. It is a Metal Oxide Semiconductor (MOS) type Gas Sensor also referred to as Chemiresistors because the detection is predicated upon change of resistance of the sensing material when the Gas comes in contact with the material. Using a simple potential divider network, concentrations of gas are often detected. MQ2 Gas sensor works on 5V DC and draws around 800mW.[6]
•	We use the MQ2 sensor to eliminate gaseous emissions in the underpass, as it will detect the level of pollution and notify the public via a warning system. The harmful gases will produce an adverse impact, if not handled properly; so, in the case of more pollution, as detected by the MQ2 sensor, we are further slowing down the traffic.

#### 2.	PIR Sensor:
A PIR Sensor or a Passive Infrared Sensor is an electronic device that measures the infrared (IR) light emitted by the objects in its observable area. The sensor actually doesn’t emit any infrared light but rather passively detects it that is emitted by its surrounding objects. Every object, with its surface temperature greater than temperature i.e. -2730 C emits heat within the sort of infrared radiation. Humans cannot see this radiation as the radiations are in infrared wavelength. But PIR Sensors detect these radiations and alter them into appropriate electrical signals. The brain of the PIR Sensor Module is that the BISS0001 PIR Motion Detector IC. 
•	We are using PIR, to detect unwanted accidents that occur in the underpass. PIR quickly spots any motion which is barely unnoticeable in heavy rainfall, thus the use of this sensor will minimize the loss of lives.

#### 3.	Camera:
•	We use a camera to ensure that the motion detected by the PIR sensor, is mainly a living being. This information is helpful in such a scenario, where immediate help is needed to save human life in case of accidents in waterlogged areas. Therefore, we need to be sure if the motion detected by the PIR sensor is specifically a human.

#### 4.	Grove - Water Level Sensor:
The Grove Water Level Sensor is a very accurate sensor which will be helpful in water level sensing applications. It is fully waterproof and uses capacitive pads to detect water levels up to 10cm. This sensor protects against moisture, dust, chemicals and high temperatures making accurate water level measurements (±5mm accuracy) easily.
•	In our project, the water level sensor will indicate an alert, if the water rises above the threshold which will automatically switch the pump to remove access of water. This is a beneficial process since no manual operation of the water pump is required.

#### 5.	LDR Sensor:
A Light Dependent Resistor (LDR) is additionally called a photoresistor or a sulfide (CdS) cell. It is also called a photoconductor. It is basically a photocell that works on the principle of photoconductivity. The passive component is essentially a resistor whose resistance value decreases when the intensity of sunshine decreases. This optoelectronic device is usually utilized in light varying sensor circuit, and lightweight and dark activated switching circuits. 
•	To overcome the lightning issue during heavy rainfall, we use LDR to automatically control the brightness of street lights.

#### 6.	Buzzer:
•	Buzzer is employed within the system to point or to grab the emergency attention occurred. Buzzer act as a panic horn which indicates the necessity of instant attention as within the condition goes haywire.

#### 7.	LCD:
LCD (Liquid Crystal Display) screen is an electronic display module and finds a good range of applications. A 16x2 LCD display is an extremely basic module and is extremely commonly used in various devices and circuits. Such modules are preferred over seven segments and other multi segment LEDs. LCDs are economical; easily programmable; have no limitation of displaying special and even custom characters (unlike in seven segments) animations then on. 
•	The LCD has two registers i.e. Command and Data. The command register stores the instructions of a command given to the LCD. A command is an instruction given to LCD to try a predefined task like initializing, clearing the screen, setting the cursor position, controlling the display, etc. The data register stores the info to be displayed on the LCD. The info is that the ASCII value of the character is displayed on the LCD.

#### 8.	Principle of Internet of Things:
The Internet of Things, or IoT, refers to the billions of physical devices worldwide that are now connected to the internet, all of which store and exchange data. Thanks to the introduction of super-cheap computer chips and the easy availability of wireless networks, everything can be converted into a part of the IoT. Connecting and attaching sensors to all of these different items brings a degree of artificial intelligence to devices that would otherwise be stupid, allowing them to exchange data in real-time without involving a human being.[5]

### IoT Protocols: -
•	Constrained Application Protocol (CoAP)
CoAP features Service Quality which is used to monitor the messages received and mark them as 'confirmable' or 'non conformable' accordingly indicating whether or not the receiver should return an 'ack.' Other important features of CoAP are that it supports the framework for content negotiation and resource exploration. 
•	Message Queuing Telemetry Transport (MQTT)
The MQTT is focused on a platform for customers, publishers, and brokers. The role of the publisher within the model is to collect the data and send information to subscribers via the mediation layer that is the broker. On the other hand, the broker's job is to ensure protection by cross-checking publisher and subscriber authorizations.
IFTTT (If This, Then That): -
•	If This Then That, also known as IFTTT, is a web-based freeware application that generates chains of simple statements of condition, called applets. Changes occurring inside other Web services such as Gmail, Facebook, Telegram, Instagram, or Pinterest cause an applet. It helps attach all of your various apps and devices. 
9.	Concept of Graphical User Interface (GUI):
GUI is an interface that permits users to interact with different electronic devices using icons and other visual indicators. The graphical user interfaces were created because command line interfaces were quite complicated and it was difficult to learn all the commands in it.
In today’s times, graphical user interfaces are used in many devices such as mobiles, MP3 players, gaming devices, smartphones etc. [7]
The below diagram provides the position of the graphical user interface with respect to the computer system –


### Elements in GUI: -

Graphical interface makes use of visual elements mostly. These elements define the appearance of the GUI. Some of these are described in detail as follows −
•	Window: -
This is the element that displays the information on the screen. It is very easy to manipulate a window. It can be opened or closed with the click of an icon. Moreover, it can be moved to any area by dragging it around. 
•	Menu: -
A menu contains a list a choice and it allows users to select one from them. A menu bar is displayed horizontally across the screen such as pull-down menu. When any option is clicked in this menu, then the pull-down menu appears.
•	Icons: -
Files, programs, web pages etc. can be represented using a small picture in a graphical user interface. This picture is known as an icon. Using an icon may be a fast thanks to open documents, run programs etc. because clicking on them yields instant access.
•	Controls: -
Information in an application can be directly read or influences using the graphical control elements. These are also known as widgets. Normally, widgets are wont to display lists of comparable items, navigate the system using links, tabs etc. 
•	Tabs: -
A tab is associated with a view pane. It mostly contains a text label or a graphical icon. Tabs are sometimes related to widgets and multiple tabs allow users to switch between different widgets. 

### SYSTEM IMPLEMENTATION
 

The operations of the system are divided into 3 levels as shown above:
LEVEL 1:
•	Arduino / Node MCU is used as a centralized unit responsible for all the input/output operations for the overall system.
•	All the input operations are done by sensor. (Water level, MQ2, PIR sensor)
•	When water level rises, a signal is sent to Arduino resulting in buzzing alert.
LEVEL 2:
•	Camera will send the live feed and visuals will be further sent to GUI. 
•	Signal is transmitted via microcontroller for performing the switching operation of relay to operate the pump. 
LEVEL 3:
•	The signal received from the water level sensor via microcontroller, results in activation of the pump after the threshold value has been reached.
•	Water collected is now being conserved for domestic purposes.
•	All the sensor values will be displayed on GUI.
•	Visuals from the camera will be live broadcasted.
Methodology for Water Conservation:
The art of water management is the effective use of water without leading to excessive wastage. To wisely limit our water intake and take good care of it, consideration is given to an improved water management scheme. Here, after cleaning it via Water Treatment Plant, all the wastewater will be collected for further use by society. 
Water is a constant, reliable source worldwide, and will not be available forever. Droughts are worthwhile issues of this water shortage by drying upland and all the life that it comprises. The land for the crops is diminishing, and more and more water is needed every day. High demands occur when food production is low which affects the economy. For our natural resources to be properly protected, actions and attitudes towards sustainability must remain at a high level while constantly preserving and using water without more waste. Such a scenario is fulfilled by our project.

