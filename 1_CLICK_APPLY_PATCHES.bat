@echo off
title Trae Peak Autonomy Auto-Patcher
echo ===================================================
echo   Trae Peak Autonomy and Reasoning Auto-Patcher
echo ===================================================
python "%~dp0apply_all_patches.py"
echo.
echo ===================================================
echo   Process Complete! Restarting Trae...
echo ===================================================
timeout /t 3 >nul 2>&1
