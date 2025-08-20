// Config
constexpr int SPEAKER1 = 12;
constexpr int SPEAKER2 = 14;
constexpr int SPEAKER3 = 27;
constexpr int SPEAKER4 = 26;

constexpr int INPUT1 = 25;
constexpr int INPUT2 = 33;
constexpr int INPUT3 = 32;
constexpr int INPUT4 = 18;

// Functions
namespace gpio
{
    int Init();
    int Deinit();
}