[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$p = & { python -V } 2>&1

$version = if ($p -is [System.Management.Automation.ErrorRecord]) {
    # grab the version string from the error message
    # $p.Exception.Message
    Write-Host "> Fazendo Download do Python" -ForegroundColor Green
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe" -OutFile "c:/temp/python-3.7.4.exe"

    Write-Host "> Fazendo a Instalação do Python" -ForegroundColor Green
    c:/temp/python-3.7.4.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

    Write-Host "> Instalando o PipEnv" -ForegroundColor Green
    pip install pipenv
}
else {
    $p
}
Write-Host $version

Write-Host "> Configurando o PipEnv para as Assinaturas" -ForegroundColor Green
pipenv install

Write-Host "> Gerando as Assinaturas" -ForegroundColor Green
pipenv shell python main.py
