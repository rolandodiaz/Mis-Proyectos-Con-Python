retiro=float(input('Ingrese valor de retiro:'))
n=float(input('Ingrese el nro de cuotas: '))
i=float(input('Ingrese la tasa de interes: '))
VC= retiro*(i*((1+i)**n)/((1+i)**n-1))
montoTotalIntereses=VC*n-retiro
print('El valor de la cuota es : %.2f'%VC,'soles.')
print('Monto total de intereses es: %.2f'%montoTotalIntereses,'soles.')