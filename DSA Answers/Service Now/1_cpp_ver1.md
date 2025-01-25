```cpp
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

// Calculate Euclidean distance
double d(pair<double, double> p1, pair<double, double> p2) {
    return sqrt(pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
}

// Calculate illuminated length of segment inside circle
double s_i(pair<double, double> a, pair<double, double> b, pair<double, double> c, double r) {
    double ax = a.first, ay = a.second;
    double bx = b.first, by = b.second;
    double cx = c.first, cy = c.second;

    double abx = bx - ax, aby = by - ay;
    double acx = cx - ax, acy = cy - ay;
    double abl = sqrt(abx * abx + aby * aby);
    double ubx = abx / abl, uby = aby / abl;

    double p = acx * ubx + acy * uby;
    double px = ax + p * ubx, py = ay + p * uby;
    double dc = d({px, py}, c);

    if (dc > r) return 0;

    double delta = sqrt(r * r - dc * dc);
    double t1 = p - delta, t2 = p + delta;
    t1 = max(0.0, t1);
    t2 = min(abl, t2);

    if (t1 > t2) return 0;
    return t2 - t1;
}

// Main function to calculate minimum dark distance
int mD(pair<double, double> a, pair<double, double> b, vector<vector<double>> &lights) {
    double td = d(a, b), il = 0;

    for (auto &l : lights) {
        double cx = l[0], cy = l[1], r = l[2];
        il += s_i(a, b, {cx, cy}, r);
    }

    double dd = td - il;
    return max(0, (int)floor(dd));
}

// Driver code
int main() {
    // Test case 1
    pair<double, double> a1 = {-2, 2};
    pair<double, double> b1 = {2, -2};
    vector<vector<double>> l1 = {{1, 1, 2}, {2, 2, 1}};
    cout << mD(a1, b1, l1) << endl; // Output: 2

    // Test case 2
    pair<double, double> a2 = {-1, -1};
    pair<double, double> b2 = {1, 1};
    vector<vector<double>> l2 = {{0, 0, 1}, {0, 0, 2}};
    cout << mD(a2, b2, l2) << endl; // Output: 0

    return 0;
}
