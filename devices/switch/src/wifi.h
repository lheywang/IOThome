#pragma once

namespace wifi
{
    int Connect();
    int Disconnect();
    int CheckStatus(bool AutoCorrect); // Set to True to enable auto patch of the status
}