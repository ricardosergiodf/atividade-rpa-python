$exclude = @("venv", "ativ-pratica-1-rpa-python.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "ativ-pratica-1-rpa-python.zip" -Force