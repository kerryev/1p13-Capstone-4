const int pinButton1 = 8;
const int pinButton2 = 7;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  int stateButton1 = digitalRead(pinButton1);
  int stateButton2 = digitalRead(pinButton2);
  
  if (stateButton1 == 1) {
    Serial.println("BUTTON 1 WAS PRESSED");
  } else if (stateButton2 == 1) {
    Serial.println("BUTTON 2 WAS PRESSED");
  } else {
    Serial.println("BUTTON WAS NOT PRESSED");
  }
  delay(500);

}
