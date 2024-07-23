# ! /bin/bash
# Programa que permite manejar las utilidades de Postres
# Autor: Marco Toscano Freire - @martosfre

opcion=0

while :
do
    #Limpiar la pantalla
    clear
    #Desplegar el menú de opciones
    echo "_________________________________________"
    echo "PGUTIL - Programa de Utilidad de Postgres"
    echo "_________________________________________"
    echo "                MENÚ PRINCIPAL           "
    echo "_________________________________________"
    echo "1. Procesos Actuales"
    echo "2. Memoria Disponible"
    echo "3. Espacio en Disco"
    echo "4. Información de Red"
    echo "5. Variables de Entorno Configuradas"
    echo "6. Información Programa"
    echo "7. Backup información"
    echo "8. Salir"

    #Leer los datos del usuario - capturar información
    read -n1 -p "Ingrese una opción [1-8]:" opcion

    #Validar la opción ingresada
    case $opcion in
        1)
            echo -e "\nProcesos Actuales....."
            sleep 3
            ;;
        2) 
            echo -e "\nMemoria Disponible...."
            sleep 3
            ;;
        3) 
            echo -e "\nEspacio en Disco..."
            sleep 3
            ;;
        4) 
            echo -e "\nInformación de Red..."
            sleep 3
            ;;
        5) 
            echo -e "\nVariables de Entorno Configuradas..."
            sleep 3
            ;;
        6) 
            echo -e "\nInformación Programa..."
            sleep 3
            ;;
        7) 
            echo -e "\nBackup información..."
            sleep 3
            ;;
        8)  
            echo -e "\nSalir del Programa"
            exit 0
            ;;
    esac
done    