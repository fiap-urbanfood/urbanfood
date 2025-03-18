#!/bin/sh
# Verifique se o MySQL está íntegro antes de aplicar as migrações e iniciar a aplicação

set -e

if [[ -n "${MYSQL_HOST}" ]] && [[ -n "${MYSQL_PORT}" ]]; then 
	echo "Validando a conexao com MySQL..."
    while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
      sleep 0.1
    done
    echo "MYSQL Iniciado"
fi

python ./manage.py makemigrations
python ./manage.py migrate
exec "$@"