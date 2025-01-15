#!/usr/bin/bash

samedi_art() {
    clear
    cat samedi.txt
}

menu() {
    echo "===MENU==="
    echo "[1] Scan Directory"
    echo "[2] Add Option in Future"
    echo "[3] Exit"
    echo "=========="
}

while true; do
    samedi_art
    menu
    echo -n "Choose option: "
    read choice
    
    case $choice in
    1)
        echo -n "Enter the website URL: "
        read url
        python3 main.py "$url"
        echo "Scan complete. Check the results file: ${url//\//_}_results.txt"
        ;;
    2)
        echo "Option will be added in the future."
        ;;
    3)  
        echo "BYE BYE"
        exit 0
        ;;
    *)  
        echo "Invalid option, try again."
        ;;
    esac
    
    echo ""
    echo "Press Enter to continue"
    read  
done