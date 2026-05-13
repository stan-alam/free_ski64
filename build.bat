@echo off
setlocal
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars32.bat"
echo === Starting Build ===
nmake -f skifree_decomp.mak CFG="skifree_decomp - Win32 Release" /DNOEXTERNALDEPS
echo === Build Finished ===
dir Release\
