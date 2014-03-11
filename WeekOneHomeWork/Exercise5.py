C=float(input('Ingrese valor de compra:'))
n=float(input('Ingrese el nro de cuotas: '))
i=float(input('Ingrese la tasa de interes: '))
VC= C*(i*((1+i)**n)/((1+i)**n-1))
montoTotalIntereses=VC*n-C
print('El valor de la cuota es : %.2f'%VC,'soles.')
print('Monto total de intereses es: %.2f'%montoTotalIntereses,'soles.')