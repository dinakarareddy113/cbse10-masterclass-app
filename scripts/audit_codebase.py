import os
import re
import json

def audit_html():
    print("=== AUDITING mobile_test/index.html ===")
    with open('mobile_test/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Screen detection
    screens = re.findall(r"screen\s*===\s*'([^']+)'", html)
    print(f"Screens in navTo: {set(screens)}")

    # 2. Check KaTeX
    has_katex = 'katex' in html.lower()
    print(f"KaTeX included: {has_katex}")
    # Check if renderMathInElement is called
    has_autorender = 'renderMathInElement' in html
    print(f"renderMathInElement called: {has_autorender}")

    # 3. Check Quiz Timer & Score Logic
    has_timer = bool(re.search(r'setInterval|clearInterval', html))
    print(f"Timer functions present: {has_timer}")
    
    # 4. Check Navigation & Quiz flow
    # Does chapter_hub have a Quiz Mode vs Practice Mode?
    hub_match = re.search(r"else if \(screen === 'chapter_hub'\) \{([\s\S]*?)(?=else if \(screen ===)", html)
    if hub_match:
        hub_code = hub_match.group(1)
        print("Chapter Hub contains:")
        print(" - Practice button:", 'chapter_practice' in hub_code)
        print(" - Formula button:", 'chapter_formulas' in hub_code)
        print(" - Quiz mode button:", 'quiz' in hub_code)

    # 5. Check Viewport and Responsive Meta tags
    viewport = re.search(r'<meta name="viewport"[^>]+>', html)
    print(f"Viewport meta tag: {viewport.group(0) if viewport else 'MISSING'}")

    # 6. Service worker for PWA offline
    print(f"Service Worker registered: {'serviceWorker.register' in html}")

    # 7. Check LocalStorage persistence keys
    ls_keys = re.findall(r"localStorage\.(?:setItem|getItem)\('([^']+)'", html)
    print(f"LocalStorage keys: {set(ls_keys)}")

    # 8. Check Error Boundaries
    print(f"window.onerror present: {'window.onerror' in html}")
    print(f"unhandledrejection present: {'unhandledrejection' in html}")

def audit_flutter():
    print("\n=== AUDITING FLUTTER CODEBASE (lib/) ===")
    for root, dirs, files in os.walk('lib'):
        for file in files:
            if file.endswith('.dart'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Check for timer leak in quiz_screen.dart
                if 'quiz_screen.dart' in file:
                    print(f"Auditing {file}:")
                    print(" - Has Timer:", 'Timer' in content)
                    print(" - Has dispose:", 'dispose()' in content)
                    print(" - Disposes timer:", 'cancel()' in content)
                    print(" - WidgetsBindingObserver (pause on background):", 'WidgetsBindingObserver' in content)
                    print(" - LocalStorage / SharedPreferences persistence:", 'SharedPreferences' in content)
                if 'quiz_provider.dart' in file:
                    print(f"Auditing {file}:")
                    print(" - Score calculation:", 'score' in content.lower())
                    print(" - Persistence:", 'prefs' in content.lower())

if __name__ == '__main__':
    audit_html()
    audit_flutter()
