// Config
constexpr int SPEAKERS[4] = {12, 14, 27, 26};
constexpr int INPUTS[4] = {25, 33, 32, 18};

// Functions
namespace gpio
{
    int Init();
    int Deinit();
}