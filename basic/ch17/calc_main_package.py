from ch17.services  import calculator1 as calculator1
from ch17.services  import calculator2 as calculator2

def  main():
    print('calculator3.add(10,2)-->', calculator1.add(10,2))
    print('calculator3.substruct(10,2)-->', calculator1.substruct(10,2))
    print('calculator3.multiply(10,2)-->', calculator2.multiply(10,2))
    print('calculator3.divide(10,2)-->', calculator2.divide(10,2))



main()