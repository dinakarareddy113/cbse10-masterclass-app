@echo off
echo =====================================================================
echo  CBSE Class 10 Masterclass - Automated Android APK Build Script
echo =====================================================================
echo.

where flutter >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Flutter SDK is not detected in your PATH.
    echo Please ensure Flutter SDK is installed and added to your System PATH:
    echo https://docs.flutter.dev/get-started/install/windows
    echo.
    echo Alternatively, push your repository to GitHub to use the automated
    echo GitHub Actions cloud builder (.github/workflows/build_apk.yml),
    echo which compiles and delivers the APK without needing local SDKs.
    pause
    exit /b 1
)

echo [1/4] Running flutter doctor...
call flutter doctor

echo.
echo [2/4] Fetching Flutter dependencies...
call flutter pub get

echo.
echo [3/4] Running unit test suite...
call flutter test

echo.
echo [4/4] Compiling Android APK (Debug / Sideloading)...
call flutter build apk --debug

echo.
echo =====================================================================
echo [SUCCESS] APK generated successfully at:
echo build\app\outputs\flutter-apk\app-debug.apk
echo =====================================================================
pause
