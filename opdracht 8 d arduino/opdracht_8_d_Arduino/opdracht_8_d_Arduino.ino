const int LED_ONE = 2;
const int LED_TWO = 3;
const int RPI_CONNECTOR = 8;

void setup() {
  pinMode(LED_ONE, OUTPUT);
  pinMode(LED_TWO, OUTPUT);
  pinMode(RPI_CONNECTOR, OUTPUT);

}

void loop() {

  if(digitalRead(RPI_CONNECTOR)){
    digitalWrite(LED_ONE, HIGH);
    digitalWrite(LED_TWO, LOW);
  } else if(!digitalRead(RPI_CONNECTOR)){
    digitalWrite(LED_ONE, LOW);
    digitalWrite(LED_TWO, HIGH);
  }

}
