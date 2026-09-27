#!/usr/bin/env bash
set -e

echo "====================================================================="
echo " CBSE Class 10 Masterclass - Android APK Build Script (Linux/macOS)"
echo "====================================================================="

if ! command -v flutter &> /dev/null; then
    echo "[ERROR] Flutter SDK could not be found."
    echo "Install Flutter from https://docs.flutter.dev/get-started/install"
    exit 1
fi

echo "[1/4] Running flutter doctor..."
flutter doctor

echo "[2/4] Fetching Flutter dependencies..."
flutter pub get

echo "[3/4] Running unit tests..."
flutter test

echo "[4/4] Building APK..."
flutter build apk --debug

echo "====================================================================="
echo "[SUCCESS] APK ready at: build/app/outputs/flutter-apk/app-debug.apk"
echo "====================================================================="
