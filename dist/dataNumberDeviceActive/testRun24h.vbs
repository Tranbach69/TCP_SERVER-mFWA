Dim oShell
Set oShell = CreateObject("WScript.Shell")
i = 0
Do While i = 0
oShell.run "dataNumberDeviceActive.exe"
WScript.Sleep(10000)
Loop