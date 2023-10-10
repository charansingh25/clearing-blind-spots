
// C++ code
long distancel, distance2, distance3, distance4;
int trigpin1=12,trigpin2=12,trigpin3=12, trigpin4=12; 
int echopin1=11, echopin2=10, echopin3=9, echopin4=6;
int duration;

void setup()
{
  pinMode (trigpin1, OUTPUT);
  pinMode (echopinl, INPUT); 
  pinMode (trigpin2, OUTPUT);
  pinMode (echopin2, INPUT); 
  pinMode (trigpin3, OUTPUT); 
  pinMode (echopin3, INPUT); 
  pinMode (trigpin4, OUTPUT); 
  pinMode (echopin4, INPUT);
  Serial.begin(9600);
}



void loop()
{

  distance1=getdistance (trigpinl, echopin1); 
  distance2=getdistance (trigpin2, echopin2); 
  distance3=getdistance (trigpin3, echopin3); 
  distance4=getdistance (trigpin4, echopin4);

  Serial.print (String (distance1));
  Serial.print(" ");
  Serial.print (String (distance2));
  Serial.print(" ");
  Serial.print(String (distance3));
  Serial.print(" ");
  Serial.println(String (distance4));
  delay(1);

}

long getdistance (int trigPin, int echoPin)
{
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds (2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds (10);
  digitalWrite(trigPin, LOW);
  // Reads the echopin, returns the sound wave travel time in microseconds duration = pulse In (echoPin, HIGH);
  // Calculating the distance
  return (duration * 0.034 / 2); // Speed of sound wave divided by 2 (go and back)
}
