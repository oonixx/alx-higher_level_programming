#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about the Python object as bytes.
 *
 * @p: The Python object to be analyzed.
 * Return: This function has no return value.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, index, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (index = 0; index < limit; index++)
		if (string[index] >= 0)
			printf(" %02x", string[index]);
		else
			printf(" %02x", 256 + string[index]);

	printf("\n");
}

/**
 * print_python_list - Prints information about the Python object as a list.
 *
 * @p: The Python object to be examined.
 * Return: This function does not return a value.
 */
void print_python_list(PyObject *p)
{
	long int size, index;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (index = 0; index < size; index++)
	{
		obj = ((PyListObject *)p)->ob_item[index];
		printf("Element %ld: %s\n", index, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
