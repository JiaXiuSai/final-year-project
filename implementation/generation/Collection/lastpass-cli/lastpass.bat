@echo off
====SETLOCAL EnableDelayedExpansion
for /L %%N in (1,1,100000) do (
lpass generate testing --no-symbol 12 >> lastpass.txt
)