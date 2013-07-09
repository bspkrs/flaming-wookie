@echo off

for /d %%I in (*) do (
  echo.
  echo Processing %%I...
  cd %%I
  if EXIST .git (
    echo Found .git, proceeding to issue pull command...
    git.exe pull -v --progress       "origin"
  ) else echo Not a Git repository, skipping...
  cd ..
)
pause