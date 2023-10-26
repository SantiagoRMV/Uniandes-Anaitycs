# Simulaci�n de Eventos Discretos
# equiposimulacion@uniandes.edu.co
#################################################

##Instalaci�n de los paquetes utilizados
#install.packages("MASS")
#install.packages("survival")
#install.packages("fitdistrplus")

##Cargar los paquetes
library(MASS)
library(survival)
library(fitdistrplus)

############################################################################################
## Cargar serie de datos:
setwd("/Users/santiagoromero/Documents/Maestria/Mejora de Procesos/Simulación/Notebooks clase/Clase 2/")
#setwd("C:/path/to/datos")
datos <- read.csv(file="mmps_clase2_datos.csv", header=TRUE, sep=",")

############################################################################################
## Histograma de la serie de datos.
hist(datos$TiempoEntreArribos, main = "Histograma de la serie de datos", xlab="Hora entre Arribos", las=1, pro = FALSE)

############################################################################################
## Pruebas de bondad y ajuste

## Almacenar la estimaci�n por m�xima verosimilitud de la serie de datos
## a una distribuci�n de probabilidad ingresada por par�metro.
ajuste <- fitdist(datos$TiempoEntreArribos, "exp")

# "beta", "cauchy", "chi-squared", "exp", "f", "gamma", "geome", "log-normal", 
# "lognormal", "logist", "negative binomial", "norm", "pois", "t" and "weibull"

## Mostrar los par�metros del ajuste a la distribuci�n dada.
print(ajuste$estimate)

## Mostrar las gr�ficas de inter�s de las distribuciones emp�rica y te�rica.
plot(ajuste)

## Realizar y guardar prueba de bondad de ajuste a la serie de datos con respecto a
## la distribuci�n te�rica escogida.
resultados <- gofstat(ajuste)

## Rechazo de la prueba de Kolmogorov-Smirnov
print(resultados$kstest)

## P-Value de la prueba de Chi-Cuadrado
print(resultados$chisqpvalue)

##############################*##############################################################
### Prueba de homogeneidad de varianzas 

#Filtrar la tabla por las 2 franjas horarias que voy a comparar
dosniveles<-datos[datos$FranjaHoraria %in% c("1", "2"), ]

#Ver tabla
View(dosniveles)

#Prueba de varianzas iguales
res.ftest<-var.test(dosniveles$TiempoEntreArribo~dosniveles$FranjaHoraria,data=dosniveles)

#Resultados test F 
res.ftest

############################################################################################
### Prueba de diferencia de medias

#Filtrar la tabla por las 2 franjas horarias que voy a comparar
dosniveles <- datos[datos$FranjaHoraria %in% c("1", "2"), ]

# Prueba de diferencia de medias
res.ttest <- t.test(dosniveles$TiempoEntreArribo~dosniveles$FranjaHoraria,data=dosniveles)

# Resultados prueba diferencia de medias
res.ttest

############################################################################################
##  Bondad de ajuste para la franja horaria 1
franjahoraria<-datos[datos$FranjaHoraria %in% c("1"), ]

## Histograma de la serie de datos.
hist(franjahoraria$TiempoEntreArribo, main = "Histograma de la serie de datos", las=1, prob=FALSE)

## Almacenar la estimaci�n por m�xima verosimilitud de la serie de datos
## a una distribuci�n de probabilidad ingresada por par�metro.
ajuste <- fitdist(franjahoraria$TiempoEntreArribo, "exp")

## Mostrar los par�metros del ajuste a la distribuci�n dada.
print(ajuste$estimate)

## Mostrar las gr�ficas de inter�s de las distribuciones emp�rica y te�rica.
plot(ajuste)

## Realizar y guardar prueba de bondad de ajuste a la serie de datos con respecto a
## la distribuci�n te�rica escogida.
resultados <- gofstat(ajuste)

## Rechazo de la prueba de Kolmogorov-Smirnov
print(resultados$kstest)

## P-Value de la prueba de Chi-Cuadrado
print(resultados$chisqpvalue)

############################################################################################
##  Bondad de ajuste para la franja horaria 2
franjahoraria<-datos[datos$FranjaHoraria %in% c("2"), ]

## Histograma de la serie de datos.
hist(franjahoraria$TiempoEntreArribo, main = "Histograma de la serie de datos", las=1, prob=FALSE)

## Almacenar la estimaci�n por m�xima verosimilitud de la serie de datos
## a una distribuci�n de probabilidad ingresada por par�metro.
ajuste <- fitdist(franjahoraria$TiempoEntreArribo, "weibull")

## Mostrar los par�metros del ajuste a la distribuci�n dada.
print(ajuste$estimate)

## Mostrar las gr�ficas de inter�s de las distribuciones emp�rica y te�rica.
plot(ajuste)

## Realizar y guardar prueba de bondad de ajuste a la serie de datos con respecto a
## la distribuci�n te�rica escogida.
resultados <- gofstat(ajuste)

## Rechazo de la prueba de Kolmogorov-Smirnov
print(resultados$kstest)

## P-Value de la prueba de Chi-Cuadrado
print(resultados$chisqpvalue)

############################################################################################
##  Bondad de ajuste para la franja horaria 3
franjahoraria<-datos[datos$FranjaHoraria %in% c("3"), ]

## Histograma de la serie de datos.
hist(franjahoraria$TiempoEntreArribo, main = "Histograma de la serie de datos", las=1, prob=FALSE)

## Almacenar la estimaci�n por m�xima verosimilitud de la serie de datos
## a una distribuci�n de probabilidad ingresada por par�metro.
ajuste <- fitdist(franjahoraria$TiempoEntreArribo, "norm")

## Mostrar los par�metros del ajuste a la distribuci�n dada.
print(ajuste$estimate)

## Mostrar las gr�ficas de inter�s de las distribuciones emp�rica y te�rica.
plot(ajuste)

## Realizar y guardar prueba de bondad de ajuste a la serie de datos con respecto a
## la distribuci�n te�rica escogida.
resultados <- gofstat(ajuste)

## Rechazo de la prueba de Kolmogorov-Smirnov
print(resultados$kstest)

## P-Value de la prueba de Chi-Cuadrado
print(resultados$chisqpvalue)