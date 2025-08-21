// Header
#include "gpio.h"

// Arduino library
#include <Arduino.h>

int gpio::Init()
{
    for (int k = 4; k > 0; k--)
    {
        pinMode(SPEAKERS[k - 1], OUTPUT);
        digitalWrite(SPEAKERS[k - 1], LOW);
    }

    for (int k = 4; k > 0; k--)
    {
        pinMode(INPUTS[k - 1], OUTPUT);
        digitalWrite(INPUTS[k - 1], LOW);
    }
    return 0;
}

int gpio::Deinit()
{

    for (int k = 4; k > 0; k--)
    {
        pinMode(SPEAKERS[k - 1], INPUT);
        pinMode(INPUTS[k - 1], INPUT);
    }

    return 0;
}