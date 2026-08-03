#!/bin/bash

dev-start () 
{
    echo "1. start postgres@17"
    echo "2. stop postgres@17"
    echo "3. окружение py venv"
    echo "4. проверрить py venv"
    echo "0. выход"

    read script

    if [ "$script" = "0" ]; then
        return
    fi

    if [ "$script" = "1" ]; then
        brew services start postgresql@17

    elif [ "$script" = "2" ]; then
        brew services stop postgresql@17

    elif [ "$script" = "3" ]; then
        echo "Activating Python virtual environment..."
        source .venv/bin/activate

    elif [ "$script" = "4" ]; then
        deactivate

    else
        echo "Invalid option. Please choose 1, 2, or 3."
    fi
}