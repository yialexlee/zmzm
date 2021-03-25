@echo off
md new
dir *.M3U8 /b>m3u8.txt
for /f "tokens=*" %%a in (m3u8.txt) do (
  echo l=%%~na
  copy /b %%~na*.ts new\%%~na.ts
)
pause