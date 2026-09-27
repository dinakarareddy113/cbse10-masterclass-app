@echo off
setlocal EnableDelayedExpansion
echo =====================================================================
echo  CBSE Class 10 Masterclass - Automated Android APK Build Script
echo =====================================================================
echo.

:: 1. Auto-configure Flutter in PATH
if exist "C:\tools\flutter\bin" (
    set "PATH=C:\tools\flutter\bin;%PATH%"
)

:: 2. Auto-configure Java JDK (JBR) from Android Studio
if exist "C:\Program Files\Android\Android Studio\jbr\bin" (
    set "JAVA_HOME=C:\Program Files\Android\Android Studio\jbr"
    set "PATH=C:\Program Files\Android\Android Studio\jbr\bin;%PATH%"
)

:: 3. Auto-configure Android SDK
if exist "%LOCALAPPDATA%\Android\Sdk" (
    set "ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk"
    set "ANDROID_SDK_ROOT=%LOCALAPPDATA%\Android\Sdk"
    set "PATH=%LOCALAPPDATA%\Android\Sdk\platform-tools;%LOCALAPPDATA%\Android\Sdk\cmdline-tools\latest\bin;%PATH%"
)

:: 4. Auto-configure Git
if exist "C:\Program Files\Git\bin" (
    set "PATH=C:\Program Files\Git\bin;%PATH%"
)

where flutter >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Flutter SDK is not detected.
    echo Expected location: C:\tools\flutter\bin
    echo.
    echo Please install Flutter or push to GitHub Actions for cloud build.
    pause
    exit /b 1
)

echo [1/3] Environment Verified:
echo   - Flutter SDK: C:\tools\flutter
echo   - Java JDK:    %JAVA_HOME%
echo   - Android SDK: %ANDROID_HOME%
echo.

echo [2/3] Fetching Flutter dependencies...
call flutter pub get

echo.
echo [3/3] Compiling Android APK (Debug / Sideloading)...
call flutter build apk --debug

echo.
if exist "build\app\outputs\flutter-apk\app-debug.apk" (
    echo =====================================================================
    echo [SUCCESS] APK generated successfully at:
    echo %CD%\build\app\outputs\flutter-apk\app-debug.apk
    echo =====================================================================
) else (
    echo =====================================================================
    echo [NOTICE] If local Gradle build is offline, push to GitHub Actions
    echo to compile in the cloud without needing local network dependencies:
    echo   git push -u origin main
    echo =====================================================================
)
pause
