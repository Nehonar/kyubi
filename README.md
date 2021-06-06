# kyubi
Api to recover data from your bank


Punto 1.

Realizar un script en python que permita hacer el login del banco de pruebas que tenemos en http://test.unnax.com/, y que imprima la información del usuario, sus cuentas y movimientos.

El script debería poder ejecutarse de la siguiente manera:

python read.py --username Y3216434F --password pperez2018

Y el resultado esperado en la terminal sería el siguiente:

# Resultado Ex:

Accounts ( 2 )
        Account Data:
                Name: Cuenta personal
                Number: ES232100123303030032
                Currency: EUR
                Balance: 352

        Total customers: 1
                Customer Data:
                        Name: Pepito Perez
                        Participation: Titular
                        Doc: Y01235813

                        Address: Carrer de Girona, 90, 08009 Barcelona

                        Emails: pepito@perez.com
                        Phones: +34 600000000

         Statements ( 6 )
                Date          |  Amount    | Balance | Concept

                2018-07-05 |    -30.0      |  352      | Bar Pepe

                2018-06-15 |    100.0     |  382      | Transferencia

                2018-06-02 |    -20.0      |  282      | Compra online

                2018-05-11 |    80.0       |  302      | Transferencia

                2018-04-01 |    -30.0      |  222      | Retiro cajero

                2018-01-03 |    -30.0      |  252      | Bar Pepe

        Account Data:
                Name: Cuenta ahorro
                Number: ES232100523522355235
                Currency: EUR
                Balance: 1322.2

        Total customers: 1
                Customer Data:
                        Name: Pepito Perez
                        Participation: Titular
                        Doc: Y01235813

                        Address: Carrer de Girona, 90, 08009 Barcelona

                        Emails: pepito@perez.com
                        Phones: +34 600000000


         Statements ( 5 )
                Date          |  Amount    | Balance   | Concept

                2018-07-25 |    -12.0      |  1322.2    | McDonalds

                2018-07-21 |    280.0     |  1334.2    | Nomina

                2018-02-12 |    280.0     |  1054.2    | Nomina

                2018-01-01 |    -20.0      |  774.2     | Compra online

                2017-07-11 |    -20.0      |  794.2     | Compra online

Punto 2.

Implementar logs de error y manejar excepciones. Implementar unit tests y seguir convenciones de nombres y principios SOLID. Se puede utilizar cualquier framework de Unit test y Mocking que se desee.

Punto 3.

Crear una api en flask o django que permita almacenar y consultar la información recolectada similar al punto 1. Para ello se recomienda utilizar un sistema de colas que gestione las tareas de lectura de cuentas recibidas.

La api contendrá los siguientes endpoints:

POST /read/${CODE}  data={username, password}

Iniciará el proceso de lectura con los datos suministrados

GET /read/${CODE}

Retornará la lectura en caso de haberse completado o un mensaje de error.

response => {

    status: DONE | ERROR | PENDING,

    data: {

        accounts: [ {name, number, currency, balance}, … ]

        customers: [ {name, participation, document, address, emails, phones}, … ]

        statements: [ {date, amount, balance, concept}, … ]

    }

}

${CODE} es un identificador de la petición y no debería poder reutilizarse para una nueva lectura.

Usar de forma coherente los códigos de estado HTTP {200, 201, 400, 404. 500, etc} 


Punto 4.

Implementar el servicio del punto 3 usando docker-compose. En el docker-compose deberían estar todas las dependencias utilizadas por el servicio del punto 3, tales como database (mysql, postgresql, mongodb), queue system (beanstalkd, rabbitmq), cache (redis), etc.