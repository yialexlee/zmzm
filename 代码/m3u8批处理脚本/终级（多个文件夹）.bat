for /d %%s in (*) do (  
    cd %%s  
    @echo off
    md new
    dir *.M3U8 /b>new\m3u8.txt
    for /f "tokens=*" %%a in (new\m3u8.txt) do (
    echo l=%%~na
    copy /b %%~na*.ts new\%%~na.ts
    )	
    cd .. 
)
pause   