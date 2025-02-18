#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>

using namespace std;

string flag = "bronco{abcdefgh}";

int sigmas[10][4] = {
    {354, 859, 63143, 63863},
    {441, 1117, 1074, 1612},
    {491, 877, 7979, 1331},
    {518, 859, 63143, 63863},
    {204, 859, 631, 6386},
    {197, 967, 223647, 5423434},
    {69, 223, 5632, 4195},
    {226, 1013, 71733, 29271},
    {10, 211, 6314, 6386},
    {504, 599, 7454, 7049},
};

int rando(int yeet)
{
    int giving = 0;
    int bet = 0;
    while (1)
    {
        if (yeet < pow(10, giving))
            break;
        giving = giving + 1;
    }
    yeet = yeet * yeet;
    if (giving % 2 == 0)
    {
        yeet = yeet * 10;
    }
    string iykyk;
    while (yeet > 0)
    {
        if (bet > giving / 2)
        {
            if (bet - 1 < giving / 2 + giving)
            {
                iykyk.insert(0, 1, (char)('0' + yeet % 10));
            }
        }
        yeet = yeet / 10;
        bet = bet + 1;
    }
    bet = 0;
    while (giving > 0)
    {
        yeet = yeet + (iykyk[giving - 1] - '0') * pow(10, bet);
        giving = giving - 1;
        bet = bet + 1;
    }
    return yeet;
}

int so_rando(int yeet)
{
    int giving = 0;
    int bet = 0;
    while (1)
    {
        if (yeet < pow(10, giving))
            break;
        giving = giving + 1;
    }
    yeet = yeet * yeet;
    if (giving % 2 == 0)
    {
        yeet = yeet * 10;
    }
    string iykyk = to_string(yeet).substr(giving - 1, giving);
    return stoi(iykyk);
}

int L(int plus, int ratio, int _plus, int blocked)
{
    // plus = m, ratio = a, _plus = c, blocked = seed
    int dubs = (ratio * blocked + _plus) % plus;
    return dubs;
}

int high(int key)
{
    string cap = to_string(key);
    cap[0] = '0';
    return stoi(cap);
}

void cook(int e, int d[], int period[] = nullptr)
{
    if (period == nullptr)
    {
        if (so_rando(L(d[1], d[2], d[3], d[0])) > 100)
        {
            if (so_rando(L(d[1], d[2], d[3], d[0])) == 144)
            {
                flag[e - 1] = char(so_rando(L(sigmas[8][1], sigmas[8][2], sigmas[8][3], sigmas[8][0])) - 335);
            }
            else if (so_rando(L(d[1], d[2], d[3], d[0])) == 449)
            {
                flag[e - 1] = char(so_rando(L(sigmas[1][1], sigmas[1][2], sigmas[1][3], sigmas[1][0])) - 30);
            }
            else
            {
                flag[e - 1] = char(so_rando(L(d[1], d[2], d[3], d[0])));
            }
        }
        else
        {
            flag[e - 1] = char(high(rando(L(d[1], d[2], d[3], d[0]))) + 48);
        }
    }
    else
    {
        if (rando(L(period[1], period[2], period[3], period[0])) == 610)
        {
            flag[e - 1] = rando(L(period[1], period[2], period[3], period[0]));
        }
        else if (so_rando(L(d[1], d[2], d[3], d[0])) > 100)
        {
            if (so_rando(L(period[1], period[2], period[3], period[0])) > 100)
            {
                {
                    flag[e - 1] = char(so_rando(L(d[1], d[2], d[3], d[0])) - so_rando(L(period[1], period[2], period[3], period[0])));
                    if (flag[e - 1] < 100)
                    {
                        flag[e - 1] = flag[e - 1] + 100;
                    }
                }
            }
            else
            {
                flag[e - 1] = char(so_rando(L(d[1], d[2], d[3], d[0])) - rando(L(period[1], period[2], period[3], period[0])));
            }
        }
    }
}

// FLAG: br4inr0t (8 chars)

int main(int argc, char **argv)
{
    // char order: 3, 4, 1, 5, 2, 7, 6, 8
    cook(rando(361) - 300 + 7, sigmas[0]);
    cook(rando(480) - 300 + 7, sigmas[2]);
    cook(rando(490) - 400 + 7, sigmas[3], sigmas[4]);
    cook(rando(539) - 900 + 7, sigmas[9]);
    cook(rando(557) - 100 + 7, sigmas[1]);
    cook(rando(819) - 700 + 7, sigmas[6]);
    cook(rando(843) - 100 + 7, sigmas[8]);
    cook(rando(906) - 200 + 7, sigmas[7], sigmas[5]);
    cout << flag << endl;
    return 0;
}