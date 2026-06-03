#include <cmath>
#include <iostream>
#include <tuple>
#include <unistd.h>

const double PI = 3.1415;
const double ToRad = PI / 180;
const double ToDeg = 1 / ToRad;

using std::cout;
using std::endl;
using std::tuple;
using std::sin;
using std::cos;

class vec2 {
public:
  double x;
  double y;
  vec2(double x, double y) {
    this->x = x;
    this->y = y;
  }
};

// 2d rotation
// x = xcos() - ysin()
// y = xsin() + ycos()
tuple<double, double> rotation(float x, float y, float rad) {
  return {
    (x * cos(rad)) - (y * sin(rad)), 
    (x * sin(rad)) + (y * cos(rad))
  };
} 
vec2 rotation(vec2 v, float rad) {
  return vec2(
	  (v.x * cos(rad)) - (v.y * sin(rad)), 
	  (v.x * sin(rad)) + (v.y * cos(rad))
  );
} 

int main() {
  double x = 1;
  double y = 0;
  double euler = 45;

  cout << "origin: (" << x << ", " << y << ")" << endl;
  auto [rot_x, rot_y] = rotation(x, y, euler * ToRad);
  cout << "rotate: (" << rot_x << ", " << rot_y << ")";
}
