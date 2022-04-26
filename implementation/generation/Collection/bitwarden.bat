@echo off
====SETLOCAL EnableDelayedExpansion
for /L %%N in (1,1,100000) do (
bw generate >> bitwarden.txt
echo.>> bitwarden.txt
)