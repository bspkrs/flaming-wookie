@setlocal enableextensions enabledelayedexpansion
@echo off

for /d %%I in (*) do (
  echo.
  echo Processing %%I...
  set dname=%%I
  set dname=!dname:_origin=!
  if NOT "%%I"=="!dname!" (
    echo Tagged as external origin, skipping...
  ) else (
    cd %%I
    if EXIST build.xml (
      echo Found build.xml, running ant...
      call ant
    ) else echo No build script found, skipping...
    cd ..
  )
)

pause