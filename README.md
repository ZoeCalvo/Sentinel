# Bienvenido a Sentinel

Sentinel es una aplicación web desarrollada como TFG del grado de ingeniería informática de la Universidad de Burgos que realiza un análisis de sentimientos de textos extraídos de las redes sociales Twitter e Instagram.

La aplicación busca los tweets relacionados con la palabra introducida en el caso de Twitter, o los comentarios que le han escrito a la cuenta de Instagram que se ha buscado.  

Después analiza el sentimiento que hay en ellos, los puntúa con valores entre 0 y 1 y se almacenan los resultados. 

Estos resultados se muestran al usuario en gráficos y tablas para hacer la experiencia más visual. Además se le ofrece la opción de calcular series temporales a partir de los resultados, y se da una predicción de los valores futuros.

## Instalación en local
Para poder utilizar la aplicación en local, es necesario instalarse los siguientes componentes: 
* **Python**: Versión 3.8
* **MySQL Installer**: Versión 8.0.20  
    * _MySQL Workbench_  
    * _MySQL Server_  
    * _MySQL Connector Python_
* **Nodejs**: Versión 12.16.1
* **Visual C++ Tools**: A partir de la versión del 2015
* **Librerías de Python**:  
    * **flask**: Versión 1.1.1  
    * **flask-cors**  
    * **tweepy.py**  
    * **LevPasha/Instagram-API-Python**  
    * **aylliote/senti-py**  
    * **TextBlob**: Versión 0.16.0  
    * **statsmodels**  
    * **pmarima**  
    

Todas las librerías de Python pueden instalarse de la misma forma:
```
$ pip install [librería]
```
Además deberás tener una cuenta de Instagram con la que poder loggearte, crearte una cuenta de desarrollador en Twitter, crear una base de datos en MySQL Workbench y obtener una clave de YandexTranslate.

Todo lo anterior es gratuito.

Cuando se hayan completado todos los requisitos anteriores, deberemos introducir las claves que nos han dado en variables de entorno. De esta forma se podrán conectar con nuestro código. 

Para saber exactamente como deben llamarse cada variable hay que acceder a los diferentes archivos .py y ver el nombre, se encuentra en mayúsculas.

Para la parte de la interfaz de usuario, deberemos instalar todos los módulos que utiliza el proyecto.

Para ello abrimos la consola:
```
$ cd frontend
$ npm install -g @angular/cli
$ npm install
$ npm start
```
Este último comando levantará el proyecto en http://localhost:4200/.

### Para ejecutar
Tras realizar la instalación, deberemos abrir dos consolas y posicionarlas en el directorio de nuestro proyecto.

En la primera consola escribiremos:
```
$ cd src
$ py server.py
```
Esto levantará el servidor en http://localhost:5000/.

En la segunda consola escribiremos:
```
$ cd frontend
$ ng serve
```
Aunque se puede utilizar el comando anteriormente visto para iniciar la interfaz de usuario, _ng serve_ es más rápido.

Esto levantará la interfaz de usuario en http://localhost:4200/.

Solo deberemos introducir en nuestro buscador la última url, ya que es desde donde interactuaremos con la aplicación.

## Aplicación desplegada
La aplicación ha sido desplegada en www.heroku.com, un sitio web que nos permite alojar nuestra aplicación de forma gratuita. 

La aplicación es accesible desde este link: https://frontsentinel.herokuapp.com/

Debido a las limitaciones de RAM que impone el plan gratuito de heroku y a la cantidad importante de servicios que contiene nuestra aplicación, el rendimiento no es el mejor. 

Por ello, se ha incluido un link desde el que descargar una máquina virtual para poder realizar pruebas más rápidamente.

## Uso de la aplicación
Para realizar un buen uso de la aplicación, el proyecto consta de una wiki del manual de usuario donde se explican todas las implementaciones de la aplicación.

Puede encontrarse en este link: https://zcs0001.gitbook.io/sentinel/.


# Welcome to Sentinel

Sentinel is a web app developed as a final project for Computer Engineering Degree from University of Burgos, which performs a sentiment analysis of texts drawn from a social networks like Twitter and Instagram.
The app searches for tweets and posts related to the word key entered talking about Twitter, or comments written to Instagram accounts.

Then it analyzes feelings in them and rates them with values between 0 and 1. Immediately results are stored.

These results are shown in charts and tables to achieve the most comprehensive visual experience. Furthermore, you are able to compute time series according to results, and also observe a prediction of future values.


## Local installation
In order to use the application locally, the following components must be installed: 
* **Python**: Version 3.8
* **MySQL Installer**: Versión 8.0.20  
    * _MySQL Workbench_  
    * _MySQL Server_  
    * _MySQL Connector Python_
* **Nodejs**: Version 12.16.1
* **Visual C++ Tools**: From version 2015
* **Librerías de Python**:  
    * **flask**: Version 1.1.1  
    * **flask-cors**  
    * **tweepy.py**  
    * **LevPasha/Instagram-API-Python**  
    * **aylliote/senti-py**  
    * **TextBlob**: Version 0.16.0  
    * **statsmodels**  
    * **pmarima**  
    

All Python libraries can be installed the same way:
```
$ pip install [library]
```
In addition, you must have an Instagram account with which to log in, create a developer account on Twitter, create a database in MySQL Workbench and obtain a YandexTranslate password.

all of the above is free.

When all the previous requirements have been completed, we must enter the keys that we have been given in environment variables. 
In this way they can connect with our code.

To know exactly how each variable should be called, you have to access the different .py files and see the name, it is in capital letters.

For user interface, we must install all the modules that the project uses.

For this we open the console:
```
$ cd frontend
$ npm install -g @angular/cli
$ npm install
$ npm start
```

This last command will raise the project in http://localhost:4200/.

### To execute
After completing the installation, we must open two consoles and position them in the directory of our project.

In the first console we will write:
```
$ cd src
$ py server.py
```

This will raise the server on http://localhost:5000/.

In the second console we will write:
```
$ cd frontend
$ ng serve
```

Although you can use the command seen above to start the user interface, _ng serve_ is faster.

This will raise the user interface on http://localhost:4200/.

We only have to enter the last url in our search engine, since it is from where we will interact with the application.

## Deployed application
The application has been deployed in www.heroku.com, a website that allows us to host our application for free. 

The application is accessible from this link: https://frontsentinel.herokuapp.com/

Due to the RAM limitations imposed by the heroku free plan and the significant number of services that our application contains, the performance is not the best.
 
For this reason, a link has been included from which to download a virtual machine in order to carry out tests more quickly.

## Application use
To make good use of the application, the project consists of a wiki of the user manual where all the implementations of the application are explained.

It can be found at this link: https://zcs0001.gitbook.io/sentinel/v/en/.
