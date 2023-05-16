#include <Python.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: PyObject
 */

void print_python_list_info(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    PyObject *item;
    PyTypeObject *type;
    Py_ssize_t i;
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        type = item->ob_type;
        printf("Element %zd: %s\n", i, type->tp_name);
    }
}
