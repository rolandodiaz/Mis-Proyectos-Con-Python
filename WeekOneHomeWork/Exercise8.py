#se importara calendar y datetime para saber cuantos dias trae el mes

import calendar
from datetime import *

#inputs
#ValorVehiculo   #ValorVehiculo
#fechaIni   #la fecha de inicio del credito
#TEA   #Tasa Efectiva Anual
#nroMeses   #nro de cuotas mensuales (Periodo de Pago)
#td   #Tasa de Seguro de Desgravamen Individual
#TVA   #Tasa de Seguro Vehicular Anual
#Portes   #Portes
valorVehiculo=float(input('Ingrese valor de vehiculo:'))
fechaIni = input('Ingrese la fecha de incio de credito: aaaa-mm-dd  ')
TEA=float(input('Ingrese valor de TEA:'))
nroMeses=float(input('Ingrese nro de meses:'))
td=float(input('Ingrese tasa de seguro de desgravamen:'))
TVA=float(input('Ingrese tasa de seguro vehicular anual:'))
Portes=float(input('Ingrese Portes:'))

TEA/=100
td/=100
TVA/=100
fechaIni=datetime.strptime(fechaIni,'%Y-%m-%d')

#Variables
#nDiasMes....#nro de dias del mes
#cuotaIni   #cuota Inicial
#montoP   #monto de prestamo
#FinancCuotas   #monto de finaciamiento en couotas
#S1   #Importe desembolsado (*Importante*)
nDiasMes=int('%s'%(calendar.monthrange(fechaIni.year-1, fechaIni.month)[1]))
cuotaIni=valorVehiculo*0.2
montoP=valorVehiculo*0.8
S1=montoP
montoFinanc=S1/2
FinancCuotas=nroMeses+1
MesPorAnio=nDiasMes/365
#formulas (a) - Tasa Nominal Anual , interes
TNA=(((1+TEA)**(1/12))-1)*(12*365/360)
i=TNA*MesPorAnio
iMes=S1*i

#formulas (b) - Tasa de Seguro de Desgravamen
TDA=td*12
d=TDA*MesPorAnio
Sd=S1*d

#formula(c) Seguro vehicular
TasaSeguroVehicAlPlazoN = TVA*MesPorAnio
SeguroVehicMensual=valorVehiculo*TasaSeguroVehicAlPlazoN

#Formulas(d) - Amortizacion
Amortizacion=montoFinanc/FinancCuotas

#calculo final
cuotaTotalMes=iMes+Sd+SeguroVehicMensual+Amortizacion+Portes

print ('La primera cuota es : %.2f'%cuotaTotalMes)