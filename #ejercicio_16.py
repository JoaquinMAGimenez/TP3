#ejercicio_16.py

from heap import HeapMax

documentos = HeapMax()

documentos.agregar('Doc Empleado 1', 1)
documentos.agregar('Doc Empleado 2', 1)
documentos.agregar('Doc Empleado 3', 1)

print(documentos.quitar(False)[0])

documentos.agregar('Doc Staff TI 1', 2)
documentos.agregar('Doc Staff TI 2', 2)
documentos.agregar('Doc gerente 1', 3)

print('                           ')
print(documentos.quitar(False)[0])
print(documentos.quitar(False)[0])

documentos.agregar('Doc Empleado 4', 1)
documentos.agregar('Doc Empleado 5', 1)
documentos.agregar('Doc Gerente 2', 3)

while(documentos.tamanio > 0):
    print('                           ')
    print(documentos.quitar(False)[0])