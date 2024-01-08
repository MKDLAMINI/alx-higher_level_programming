#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <time.h>

/**
 * print_python_list_info - prints python lists
 * @p: PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	struct timespec ts;
	clock_gettime(CLOCK_REALTIME, &ts);
	printf("[*] Current time: %ld seconds, %ld nanoseconds\n", ts.tv_sec, ts.tv_nsec);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
