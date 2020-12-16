#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *item;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
