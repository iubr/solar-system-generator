# distutils: language = c++

from libcpp.vector cimport vector
cdef extern from "cintegrate.h":
    double trapezoid(const vector[double]& x, const vector[double]& y)

# Python wrapper
def ctrapezoid(list x, list y):
    cdef vector[double] cx
    cdef vector[double] cy
    for val in x:
        cx.push_back(val)
    for val in y:
        cy.push_back(val)
    return trapezoid(cx, cy)
