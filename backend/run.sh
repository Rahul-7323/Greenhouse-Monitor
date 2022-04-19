venv=".env"

if [ -d $venv ]; then
    echo "Activating virtual environment"
    echo "Starting the application"
    . ${venv}/bin/activate
    export ENV="DEVELOPMENT"
    export SECRET_KEY='u8Sj>VmmG,$X!tAA&{A,iDBt?9D8~J7!3O[yKW8XU|{dlZ:k|ZTZI},BCg'
    export SECURITY_PASSWORD_SALT='u@8(YLSt<UB6eNsn={SHbd9ZA*[]I}cI!*|X8]J#O:|.>RZ7DQe>9(mUw.a8d'
    gunicorn main:app
    echo "deactivating virtual environment"
    deactivate
else
    echo "No virtual environment present, run setup..."
fi;