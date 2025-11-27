includes Test;
configuration TestAppC{
}
implementation {
        components MainC, TestC, LedsC;
        components new TimerMilliC();

        TestC.Boot -> MainC;
        TestC.Leds -> LedsC;

        TestC.MilliTimer -> TimerMilliC;

        components new SensirionSht11C() as Sht11Ch0C;
        TestC.ReadTemp -> Sht11Ch0C.Temperature;
        TestC.ReadHumi -> Sht11Ch0C.Humidity;
        
        components new IlluAdcC() as Illu;
        TestC.ReadIllu -> Illu;
}
