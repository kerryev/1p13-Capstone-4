const int pinButton1 = 8;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int stateButton1 = digitalRead(pinButton1);
  
  if (stateButton1 == 1) {
    Serial.println("BUTTON 1 WAS PRESSED");
  } else {
    Serial.println("BUTTON WAS NOT PRESSED");
  }
  delay(1000);

}
