const int BUTTON = 2;
const int RPI_CONNECTOR = 8;
boolean buttonState = false;

void setup() {
pinMode(BUTTON, INPUT);
pinMode(RPI_CONNECTOR, OUTPUT);
Serial.begin(9600);

}

void loop() {

  if(digitalRead(BUTTON) && !buttonState){
    buttonState = true;
    
    if(digitalRead(RPI_CONNECTOR)){
      digitalWrite(RPI_CONNECTOR, LOW);
    } else {
      digitalWrite(RPI_CONNECTOR, HIGH);
    }

  } else if (!digitalRead(BUTTON)) {
    buttonState = false;
  }


}
