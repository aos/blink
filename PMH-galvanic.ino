unsigned long sendTime;
long average;
int points[32];
int n = 1;
byte i;
byte j;

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
  sendTime = millis() + 500;
}

void loop() {
  // send the value of analog input 0:
  if (millis() > sendTime) {
    j = 0;
    while (j < 32)
    {
      average = average  + points[j];
      j++;
    }
    average = average / 32;
    Serial.println(points[0]);
    sendTime = millis() + 10;
  }
  else {
    points[i] = analogRead(A0);
    i++;
    if (i == 32) i = 0;

  }
}
