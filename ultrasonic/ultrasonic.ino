const int trigPin1 = 9;
const int trigPin2 = 3;

const int echoPin1 = 10;
const int echoPin2 = 11;
// defines variables
long duration1;
long duration2;

int distance1;
int distance2;

void setup() {
pinMode(trigPin1, OUTPUT);// Sets the trigPin as an Output
pinMode(trigPin2, OUTPUT);
pinMode(echoPin1, INPUT); // Sets the echoPin as an Input
pinMode(echoPin2, INPUT);
Serial.begin(9600); // Starts the serial communication
}
void loop() {
 // if (Serial.available()>0)
//  {
// Clears the trigPin
digitalWrite(trigPin1, LOW);
digitalWrite(trigPin2,LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin1, HIGH);
digitalWrite(trigPin2,HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
digitalWrite(trigPin2,LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration1 = pulseIn(echoPin1, HIGH);
duration2 = pulseIn(echoPin2,HIGH);
// Calculating the distance
distance1 = duration1*0.034/2;
distance2 = duration2*0.034/2;

// Prints the distance on the Serial Monitor
//Serial.print("Distance: ");
//String dataread = String((distance/1024)*5);
Serial.println(distance1);
delay(2000);
Serial.println(distance2);

delay(2000);
//Serial.write(distance);
  }
//}
