@echo off
:start
echo 启动bpmnx. . .
java -jar D:\tools\springcloud-bpmnx-1.4.1.war

Rem 打开日志
echo 打开bpmnx日志. . . .
tail -f D:\tools\logs\info.log