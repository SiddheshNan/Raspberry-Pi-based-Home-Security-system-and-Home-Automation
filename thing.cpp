#include <stdio.h>
#include <wiringPi.h>
#include <iostream>
#include "thinger/thinger.h"

#define	DEVICE_1_PIN 4
#define DEVICE_2_PIN 5

#define USER_ID             ""
#define DEVICE_ID           ""
#define DEVICE_CREDENTIAL   ""

std::string on_v = "ON";
std::string off_v = "OFF";

int main(int argc, char *argv[])
{

	thinger_device thing(USER_ID, DEVICE_ID, DEVICE_CREDENTIAL);
	wiringPiSetup();
	pinMode(DEVICE_1_PIN, OUTPUT);
	pinMode(DEVICE_2_PIN, OUTPUT);
	

	
	thing["device1_stat"] >> [](pson& out){
		if(!digitalRead(DEVICE_1_PIN))
		{
			out = on_v;
		}
		else
		{
			out = off_v;
		}
	};
	
	thing["device2_stat"] >> [](pson& out){
		if(!digitalRead(DEVICE_2_PIN))
		{
			out = on_v;
		}
		else
		{
			out = off_v;
		}
	};
	
	
	thing["Device1"] << [](pson& in){
		if(in.is_empty())
		{
			in = !(bool) digitalRead(DEVICE_1_PIN);
		}
		else
		{
			digitalWrite(DEVICE_1_PIN, in ? LOW : HIGH);
		}
	};
	
	thing["Device2"] << [](pson& in){
		if(in.is_empty())
		{
			in = !(bool) digitalRead(DEVICE_2_PIN);
		}
		else
		{
			digitalWrite(DEVICE_2_PIN, in ? LOW : HIGH);
		}
	};

	delay (200) ;
	digitalWrite (DEVICE_1_PIN, HIGH) ; 
	digitalWrite (DEVICE_2_PIN, HIGH) ;
	delay (100) ;
	
    thing.start();
    return 0;
}
