Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c notifier.bat"
oShell.Run strArgs, 0, false