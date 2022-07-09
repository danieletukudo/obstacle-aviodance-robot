#include <Servo.h>
#define SERVO_PIN     9  //servo connect to D9
Servo myservo;
void setup() {
  myservo.attach(SERVO_PIN); // 
  myservo.write(90);//turn to middle posiztion
}

void loop() {
}
