char data;
int pin = 13;
void setup() {
  pinMode(pin,OUTPUT);
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  if(Serial.available()>0)
  {
    data = Serial.read();
    Serial.print(data);

    if(data=='1')
    digitalWrite(pin,HIGH);
    else if(data=='0')
    digitalWrite(pin,LOW);
  }
  // put your main code here, to run repeatedly:

}
