# ProGuard/R8 Rules for CBSE Class 10 Masterclass Android Release Build

# Flutter Engine Keep Rules
-keep class io.flutter.app.** { *; }
-keep class io.flutter.plugin.**  { *; }
-keep class io.flutter.util.**  { *; }
-keep class io.flutter.view.**  { *; }
-keep class io.flutter.** { *; }
-keep class io.flutter.plugins.**  { *; }

# Keep native methods
-keepclasseswithmembernames class * {
    native <methods>;
}

# Keep FlutterGeneratedPluginRegistrant
-keep class io.flutter.plugins.GeneratedPluginRegistrant { *; }

# Supabase and Postgrest serialization / models
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}
-keepattributes *Annotation*,Signature,InnerClasses,EnclosingMethod

# Hive Local Database
-keep class io.hivedb.** { *; }
-dontwarn io.hivedb.**

# Kotlin Coroutines and Reflection
-dontwarn kotlinx.coroutines.**
-keepnames class kotlinx.coroutines.** { *; }

# Suppress warnings for unused optional dependencies
-dontwarn javax.annotation.**
-dontwarn org.bouncycastle.**
