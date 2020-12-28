const int trigPin1 = 9;
const int trigPin2 = 3;
const int ir1 = A0;
const int ir2 = A1;
const int ir3 = A2;
const int ir4 = A3;
const int ir5 = A4;

const int echoPin1 = 10;
const int echoPin2 = 6;
// defines variables
long duration1;
long duration2;
int ir;
int ir21;
int ir31;
int ir41;
int ir51;
int distance1;
int distance2;

void setup() {
pinMode(trigPin1, OUTPUT);// Sets the trigPin as an Output
pinMode(trigPin2, OUTPUT);
pinMode(ir1,INPUT);
pinMode(ir2,INPUT);
pinMode(echoPin1, INPUT); // Sets the echoPin as an Input
pinMode(echoPin2, INPUT);
Serial.begin(9600); // Starts the serial communication
}
void loop() {
 // if (Serial.available()>0)
//  {
// Clears the trigPin
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);
digitalWrite(trigPin2,LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin2,HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
digitalWrite(trigPin2,LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration1 = pulseIn(echoPin1, HIGH);
duration2 = pulseIn(echoPin2,HIGH);
ir = analogRead(ir1);
ir21 = analogRead(ir2);
ir31 = analogRead(ir3);
ir41 = analogRead(ir4);
ir51 = analogRead(ir5);
// Calculating the distance
distance1 = duration1*0.034/2;
distance2 = duration2*0.034/2;

// Prints the distance on the Serial Monitor
//Serial.print("Distance: ");
//String dataread = String((distance/1024)*5);
Serial.println(distance1);
delay(1000);
Serial.println(duration2);
delay(1000);
Serial.println(ir);
delay(1000);
Serial.println(ir21);
delay(1000);
Serial.println(ir31);
delay(1000);
Serial.println(ir41);
delay(1000);
Serial.println(ir51);
delay(1000);
//Serial.write(distance);
  }
//}
