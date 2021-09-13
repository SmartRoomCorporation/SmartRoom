#include "mbed.h"
#include "XNucleoIKS01A2.h"
Serial pc (USBTX, USBRX);
Serial esp(PA_9, PA_10);

Ticker sens_time;
Thread readThread;

float temp = 0.0;
float hum = 0.0;
float press = 0.0;

char buffer[10];

bool flag = false;
int led_val = 0;

static XNucleoIKS01A2 *meb = XNucleoIKS01A2::instance(D14, D15, D4, D5);
DigitalOut led(LED1);
static HTS221Sensor *hum_temp = meb->ht_sensor;
static LPS22HBSensor *press_temp = meb->pt_sensor;
void measure(){
    flag = true;
}
void change_led(){
    if(led_val == 0){
        led = false;
    }else{
        led = true;
    }
}
void read_led(){
     while(1){
        //printf("Thread 2 \n");
        if(esp.readable()){
            printf("Received Serial Command\n");
            int num;
            buffer[0] = esp.getc();
            buffer[1] = '\0';
            num = atoi(buffer);
            pc.printf("Il valore letto è %d", num);
            led_val = num;
            change_led();
        }
        ThisThread::sleep_for(200);
    }
}
int main()
{
    pc.baud(9600);
    esp.baud(9600);
    readThread.start(read_led);
    sens_time.attach(&measure, 2);
    hum_temp->enable();
    press_temp->enable();

    while (true) {
        if(flag){
            hum_temp->get_temperature(&temp);
            hum_temp->get_humidity(&hum);
            press_temp->get_pressure(&press);   
            pc.printf("Temperature : %f\n", temp);
            pc.printf("Humidity : %f\n", hum);
            pc.printf("Pressure : %f\n", press);
            esp.printf("%f#%f#%f",temp, hum, press);
            flag = false;
        } 
        ThisThread::sleep_for(2000);
    }
}

