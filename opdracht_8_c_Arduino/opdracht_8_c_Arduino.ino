const int ARDUINO_TO_RPI_PIN = 13;
const int RPI_TO_ARDUINO_PIN = 12;
const int RPI_TO_ARDUINO_PIN_TWO = 7;
const int BUTTON_PIN = 11;
const int LED[] = {8, 9};
const int LED_OUTPUT[] = {LOW, HIGH};
int isActivated = false;

void setup() {
  pinMode(LED[0], OUTPUT);
  pinMode(LED[1], OUTPUT);
  pinMode(BUTTON_PIN, INPUT);
  pinMode(ARDUINO_TO_RPI_PIN, OUTPUT);
  pinMode(RPI_TO_ARDUINO_PIN, INPUT);
  pinMode(RPI_TO_ARDUINO_PIN_TWO, INPUT);

  digitalWrite(LED[0], LED_OUTPUT[1]);
  digitalWrite(LED[1], LED_OUTPUT[0]);
  digitalWrite(ARDUINO_TO_RPI_PIN, LED_OUTPUT[0]);

}

void loop() {
  if(digitalRead(BUTTON_PIN) && !isActivated){
    isActivated = true;
    digitalWrite(ARDUINO_TO_RPI_PIN, HIGH);
  }

  if(RPI_TO_ARDUINO_PIN){
    digitalWrite(LED[0], LED_OUTPUT[1]);
    digitalWrite(LED[0], LED_OUTPUT[0]);
  }

  if(!digitalRead(BUTTON_PIN)){
    isActivated = false;
  }

}
