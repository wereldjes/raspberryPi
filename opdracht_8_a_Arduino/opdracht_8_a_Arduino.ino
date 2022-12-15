const int RPI_LED_TWO = 13;
const int RPI_LED_THREE = 12;
const int led[] = {8, 9};

void setup() {
  pinMode(led[0], OUTPUT);
  pinMode(led[1], OUTPUT);
  pinMode(RPI_LED_TWO, INPUT);
  pinMode(RPI_LED_THREE, INPUT);
}

void loop() {
  if(digitalRead(RPI_LED_TWO)){
    digitalWrite(led[0], HIGH);
    digitalWrite(led[1], LOW);
  } else {
    digitalWrite(led[0], LOW);
    digitalWrite(led[1], HIGH);
  }
}
