#include <IRremote.h>

const int IR_SENSOR = 2;
const int RPI_PIN_ONE = 8;
const int RPI_PIN_TWO = 9;
const int RPI_PIN_THREE = 10;
const int RPI_PIN_FOUR = 11;
IRrecv receiver(IR_SENSOR);
decode_results result;
int tempPinSelected = false;

void setup() {
  receiver.enableIRIn();
  Serial.begin(9600);
  pinMode(RPI_PIN_ONE, OUTPUT);
  pinMode(RPI_PIN_TWO, OUTPUT);
  pinMode(RPI_PIN_THREE, OUTPUT);
  pinMode(RPI_PIN_FOUR, OUTPUT);
  digitalWrite(RPI_PIN_ONE, LOW);
  digitalWrite(RPI_PIN_TWO, LOW);
  digitalWrite(RPI_PIN_THREE, LOW);
  digitalWrite(RPI_PIN_FOUR, LOW);

}

void loop() {
  if(receiver.decode(&result)){
    if(!tempPinSelected){
      selectLed(result.value);
      tempPinSelected = true;
    } else if(tempPinSelected) {
      selectedSpeed(result.value);
      tempPinSelected = false;
    }

    IrReceiver.resume();
  }
  
}

void selectLed(int hex){
  switch(hex) {
    case 0xFF30CF:
      digitalWrite(RPI_PIN_ONE, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_ONE, LOW);
      break;
    case 0xFF18E7:
      digitalWrite(RPI_PIN_TWO, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_TWO, LOW);
      break;
    case 0xFF7A85:
      digitalWrite(RPI_PIN_THREE, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_THREE, LOW);
      break;
    case 0xFF10EF:
      digitalWrite(RPI_PIN_FOUR, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_FOUR, LOW);
      break;
  }
}

void selectedSpeed(int hex) {
  switch(hex) {
    case 0xFF30CF:
      digitalWrite(RPI_PIN_ONE, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_ONE, LOW);
      break;
    case 0xFF18E7:
      digitalWrite(RPI_PIN_TWO, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_TWO, LOW);
      break;
    case 0xFF7A85:
      digitalWrite(RPI_PIN_THREE, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_THREE, LOW);
      break;
    case 0xFF10EF:
      digitalWrite(RPI_PIN_FOUR, HIGH);
      delay(500);
      digitalWrite(RPI_PIN_FOUR, LOW);
      break;
  }
}
