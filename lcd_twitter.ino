#include <Servo.h>
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Servo leftWheel,rightWheel;  // create servo object to control a servo
char line[17];
char oldLine[17];
int charCnt=0;
int lineCnt=0;
int leftIn=6,rightIn=7;
void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("#sccmakes");
  Serial.begin(9600);
  line[16]=0;
  oldLine[16]=0;
  leftWheel.attach(9);
  rightWheel.attach(10);
  pinMode(leftIn,INPUT);
  pinMode(rightIn,INPUT);
}

void loop() {
  // when characters arrive over the serial port...
  //lcd.print(Serial.read());
  //delay(100);
  if (digitalRead(rightIn)){
    rightWheel.write(10);
  } else {
    rightWheel.write(90);
  }
  if (digitalRead(leftIn)){
    leftWheel.write(170);
  } else {
    leftWheel.write(90);
  }
  if (Serial.available()>0) {
    // wait a bit for the entire message to arrive
    //delay(100);
    // clear the screen
    lcd.clear();
    charCnt=0;
    lineCnt=0;
    // read all the available characters
    while (Serial.available() > 0) {
      // display each character to the LCD
      line[charCnt]=Serial.read();
      //lcd.write(byte(Serial.read()));//);
      delay(100);
      //lcd.write(line[charCnt]);
      charCnt++;
      if (charCnt>=16){
        charCnt=0;
        lineCnt++;
      if (lineCnt==1){
        lcd.print(line);
        //delay(500);
      } 
      else if (lineCnt==2){
          lcd.setCursor(0,2);
          lcd.print(line);
        delay(500);
       }
       else if (lineCnt>2){
        lcd.clear();
        //lcd.setCursor(0,1);
        lcd.print(oldLine);
        lcd.setCursor(0,2);
        lcd.print(line);
        delay(500);
      }
       for (int i=0;i<16;i++){
          oldLine[i]=line[i];
          line[i]=' ';
        }
      }
    }
    lcd.clear();
        //lcd.setCursor(0,1);
    lcd.print(oldLine);
    lcd.setCursor(0,2);
    lcd.print(line);
  }
}
