/* 
 * Adapted from Python to C++ with help from ChatGPT.
 */

#include "cintegrate.h"

double trapezoid(const std::vector<double>& x,
                 const std::vector<double>& y)
{
    std::size_t n = x.size();
    if (n < 2 || y.size() != n) {
        return 0.0;
    }

    double integral = 0.0;

    double x0 = x[0];
    double y0 = y[0];

    for (std::size_t i = 1; i < n; ++i) {
        double x1 = x[i];
        double y1 = y[i];

        double dx = x1 - x0;
        integral += 0.5 * dx * (y1 + y0);

        x0 = x1;
        y0 = y1;
    }

    return integral;
}
