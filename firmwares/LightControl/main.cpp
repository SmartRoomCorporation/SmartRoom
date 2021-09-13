#include "mbed.h"
#define LED PC_8
#define PHRES PA_0
void increaseLight(); //function to increase the light
void decreaseLight(); //funcion to decrese the light
void updateLight(); //function to update the pwm
void readSoglia(); //function to read the value of the threshold from externa serial imput
void itoa(int n, char s[]); //convert a integer into a string
void decreseFreq(float n); //decrease the frequence of the pwm
void increaseFreq(float n); //increase the frequence of the pwm

Thread readThread; //thread for reading through the external serial

int soglia = 40000; //threshold 
int currLight = 0; //current value measured from the photoresistor
float freq = 0.0; //frequency of the pwm

const int MAXSOGLIA = 40000; //max value of the light
const int MINSOGLIA = 500; //min value of the light
const float MAXFREQ = 1; //max frequency of the pwm
const float MINFREQ = 0; //min frequecy of the pwm
const int SCARTO = 300; //delta
char buffer[10]; //buffer used to send data to the serial communication

AnalogIn phres(PHRES);
PwmOut my_pwm(LED);
BufferedSerial pc(PA_11, PA_12); 

int main(){
    my_pwm.period_ms(10);//set the period of the pwm
    my_pwm.write(freq);//set initial frequecy of the pwm
    readThread.start(readSoglia); //start the readThread. The Thread execute the code from the readSoglia function
    while (true) {
        //my_pwm.write(0.5);
        updateLight(); //update the light
        itoa(currLight, buffer); //convert the value of the light in to a string 
        pc.write(buffer, sizeof(buffer)); //send data to the external serial
        printf("Current light value%s \n", buffer); //debug line
        ThisThread::sleep_for(2000ms); //thread sleep (wait 2s to send another measurement)
    }
}

/*
IncreaseLight function. The function increases the light gradually with three different speed.
To increase the light it increases the frequecy of the pwm.
*/
void increaseLight(){
    int diff = soglia - currLight; //calculate the difference between current light and threshold(soglia)

    if(diff >= 10000)increaseFreq(0.1); //if the diff is in order of 10000 increase rapidly the frequecy
    else if(diff >= 5000)increaseFreq(0.01); //if the diff is in order of 5000 increase the frequecy at medium speed
    else increaseFreq(0.001); //if diff order is small increase the frequecy slowly
}

/*
DecreseLight function. The function decreses the light gradually with three different speed.
To decrese the light it decreses the frequecy of the pwm.
*/
void decreaseLight(){
    int diff = currLight - soglia;//calculate the difference between current light and threshold(soglia)

    if(diff >= 10000)decreseFreq(0.1);//if the diff is in order of 10000 decrese rapidly the frequecy
    else if(diff >= 5000)decreseFreq(0.01);//if the diff is in order of 5000 decrese the frequecy at medium speed
    else decreseFreq(0.001);//if diff order is small decrese the frequecy slowly
}

/*
decreseFreq function. The function decrease the frequency of the pwm of the value of the parameter
*/
void decreseFreq(float n){
    if(freq > 0.1){//if the freq is greather then 0.1 decrease the frequency
        freq -= n; 
    }else{//else put the frequency to 0
        freq = 0;
    }

    my_pwm.write(freq); //update the frequecy
}

/*
decreseFreq function. The function increase the frequency of the pwm of the value of the parameter
*/
void increaseFreq(float n){
    if(freq < 0.9){//if the freq is less then 0.9 increase the frequecy 
        freq += n;
    }else{//else put the frequecy to 1
        freq = 1.0;
    }
    my_pwm.write(freq); //update the frequency
}

void updateLight(){
    currLight = phres.read_u16();
    if(currLight > soglia + SCARTO){
        decreaseLight();
    }else if(currLight < soglia - SCARTO){
        increaseLight();
    }
}

void readSoglia(){
    //lettura della soglia da seriale
    while(1){
        //printf("Thread 2 \n");
        if(pc.readable()){
            printf("Received Serial Command");
            int num = 0;
            pc.read(buffer, sizeof(buffer));
            num = atoi(buffer);
            printf("Il valore letto è %d", num );
            if(num >= MAXSOGLIA)soglia = MAXSOGLIA;
            else if(num <= MINSOGLIA)soglia = MINSOGLIA;
            else soglia = num;
            
        }
        ThisThread::sleep_for(1000ms);
    }
}
void reverse(char *s){
    char *j;
    int c;

    j = s + strlen(s) - 1;
    while(s < j) {
        c = *s;
        *s++ = *j;
        *j-- = c;
    }
}
void itoa(int n, char s[]){
    int i, sign;

    if ((sign = n) < 0)  /* record sign */
        n = -n;          /* make n positive */
    i = 0;
    do {       /* generate digits in reverse order */
        s[i++] = n % 10 + '0';   /* get next digit */
    } while ((n /= 10) > 0);     /* delete it */
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}
