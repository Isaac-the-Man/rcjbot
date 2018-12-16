#include <ros.h>
#include <rcjbot/MotorValues.h>

ros::NodeHandle  nh;

void motorCb(const rcjbot::MotorValues& motor_values){
  if (motor_values.left_power > 100){
    //digitalWrite(LED_BUILTIN, HIGH);
    nh.loginfo("on");
  }else{
    //digitalWrite(LED_BUILTIN, LOW);
    nh.loginfo("off");
  }
}

ros::Subscriber<rcjbot::MotorValues> sub("main", &motorCb);

void setup(){
  Serial.begin(9600);
  //Serial.println("Setup!");
  nh.initNode();
  nh.subscribe(sub);
}

void loop(){
  nh.spinOnce();
  delay(1);
}

