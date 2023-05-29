#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)(p))->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	size = size + 1 > 10 ? 10 : size + 1;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		if (i > 0)
			printf(" ");
		printf("%02hhx", str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float objects
 * @p: Pointer to the Python object
 */
void print_python_float(PyObject *p)
{
	char *str;
	double value;

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %lf\n", ((PyFloatObject *)(p))->ob_fval);
}
