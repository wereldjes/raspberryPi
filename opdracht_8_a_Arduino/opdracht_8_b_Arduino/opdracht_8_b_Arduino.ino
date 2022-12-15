const int RPI_LED_TWO = 13;
const int RPI_LED_THREE = 12;
const int led[] = {8, 9};
const int output[] = {LOW, HIGH};

void setup() {
  pinMode(led[0], OUTPUT);
  pinMode(led[1], OUTPUT);
  pinMode(RPI_LED_TWO, INPUT);
  pinMode(RPI_LED_THREE, INPUT);
}

void loop() {
  if(digitalRead(RPI_LED_TWO)){
    digitalWrite(led[0], output[1]);
  } else {
    digitalWrite(led[0], output[0]);
  }

  if(digitalRead(RPI_LED_THREE)){
    digitalWrite(led[1], output[1]);
  } else {
    digitalWrite(led[1], output[0]);
  }
  
}
