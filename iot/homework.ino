#include <IRremote.h>
#include <Servo.h>

const int RECV_PIN = 7;
const int relayInPin = 2; 

// Define IR Receiver and Results Objects
IRrecv irrecv(RECV_PIN);
decode_results results;
Servo myservo; 

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
  myservo.attach(5);
  pinMode(relayInPin, OUTPUT);
  digitalWrite(relayInPin, HIGH);
}

void loop(){
  if (irrecv.decode(&results)){
    Serial.println(results.value, HEX);
    if (results.value==0x5E7DB3DC){
      pumping(0, 2000); // pumping first plants for 10s
      pumping(90, 2500); // pumping first plants for 15s
      pumping(180, 5000); // pumping first plants for 20s
      }
    irrecv.resume(); 
  }
}

void pumping(int pos, int sec){
  myservo.write(pos);              // tell servo to go to position in variable 'pos'
  delay(50);                       // waits 50ms for the servo to reach the position
  digitalWrite(relayInPin, LOW);
  delay(sec);
  digitalWrite(relayInPin, HIGH); 
  delay(2000);                    // waits 2s for the water to clean
  }