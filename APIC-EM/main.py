from funciones import *
import requests
import json
import time
from path_trace import path_trace
import time

option = "0"

while option != "5":

    print(
            """
        * * * * * * * * * * * * * * * * * * * *
        *                                     *
        *   1)Get Ticket                      *
        *                                     *
        *   2)Print Hosts                     *
        *                                     *
        *   3)Print Devices                   *
        *                                     *
        *   4)Path_trace                      *
        *                                     *
        *   5)Exit                            *
        *                                     *
        * * * * * * * * * * * * * * * * * * * *
            """
        )

    option = input(">>>>>")
#Selección de opciones, ejecución de funciones
    if (option == "1"):
        ticket = get_ticket ()
        print("Ticket number: ", ticket)
        time.sleep(5.0)

    elif (option == "2"):
        print_hosts ()
        time.sleep(10.0)

    elif (option == "3"):
        print_devices ()
        time.sleep(20.0)
    elif (option == "4"):
        path_trace ()

    elif (option == "5"):
        print("See you soon ;) ")
        break

    else:
        print("***********************OPCIÓN INCORRECTA*************************")
        time.sleep(2.5)