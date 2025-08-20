// Header
#include "gpio.h"

// Arduino library
#include <Arduino.h>

int gpio::Init()
{
    pinMode(SPEAKER1, OUTPUT);
    pinMode(SPEAKER2, OUTPUT);
    pinMode(SPEAKER3, OUTPUT);
    pinMode(SPEAKER4, OUTPUT);

    pinMode(INPUT1, OUTPUT);
    pinMode(INPUT2, OUTPUT);
    pinMode(INPUT3, OUTPUT);
    pinMode(INPUT4, OUTPUT);

    digitalWrite(SPEAKER1, LOW);
    digitalWrite(SPEAKER2, LOW);
    digitalWrite(SPEAKER3, LOW);
    digitalWrite(SPEAKER4, LOW);

    digitalWrite(INPUT1, LOW);
    digitalWrite(INPUT2, HIGH);
    digitalWrite(INPUT3, LOW);
    digitalWrite(INPUT4, LOW);

    return 0;
}

int gpio::Deinit()
{
    pinMode(SPEAKER1, INPUT);
    pinMode(SPEAKER2, INPUT);
    pinMode(SPEAKER3, INPUT);
    pinMode(SPEAKER4, INPUT);

    pinMode(INPUT1, INPUT);
    pinMode(INPUT2, INPUT);
    pinMode(INPUT3, INPUT);
    pinMode(INPUT4, INPUT);

    return 0;
}