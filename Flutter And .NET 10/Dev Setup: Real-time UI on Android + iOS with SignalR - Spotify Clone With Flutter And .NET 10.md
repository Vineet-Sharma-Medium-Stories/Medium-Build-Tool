# Dev Setup: Real-time UI on Android + iOS with SignalR - Spotify Clone With Flutter And .NET 10

## Complete Development Environment Setup for Flutter Mobile App with Azure Deployment

**Subtitle:** *Step-by-step guide to setting up your Flutter development environment, configuring Spotify OAuth, implementing SignalR client, and deploying to Azure App Service with all enterprise features*

**Reference:** This setup guide works with the backend environment described in **"Dev Setup: SignalR with .NET 10 API - Spotify Clone With Flutter And .NET 10"**. For complete backend setup including .NET 10 API, SignalR Hub, and Azure deployment, please refer to the companion guide.

---

## Table of Contents (as paragraphs for flow)

This comprehensive development environment setup guide covers everything from installing Flutter SDK and configuring your development machine to deploying a production-ready Spotify analytics app to Azure. You will learn how to set up Android and iOS emulators, configure Spotify OAuth credentials, install all necessary dependencies including SignalR client and Hive for local storage, implement the complete 22-screen architecture in your IDE, configure Firebase for push notifications, set up code signing for iOS, and finally deploy to Azure App Service with CI/CD pipelines. The guide includes detailed troubleshooting sections for common issues like WebSocket connection failures, rate limiting errors, and offline sync problems, as well as performance optimization checklists for both Android and iOS builds.

---

## Part 1: Flutter Development Environment Setup

### 1.1 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 64-bit / macOS 11 / Linux Ubuntu 20.04 | Windows 11 / macOS 14 / Ubuntu 22.04 |
| **RAM** | 8 GB | 16 GB or more |
| **Storage** | 10 GB free | 50 GB SSD |
| **CPU** | 4 cores | 8 cores |
| **Internet** | Broadband | Fiber (100+ Mbps) |

### 1.2 Installing Flutter SDK

**Windows Installation:**

```powershell
# Download Flutter SDK from official site
# Extract to C:\src\flutter

# Add to PATH environment variable
$env:Path += ";C:\src\flutter\bin"

# Run Flutter doctor to verify installation
flutter doctor -v

# Accept Android licenses
flutter doctor --android-licenses
```

**macOS Installation:**

```bash
# Using Homebrew (recommended for macOS)
brew install --cask flutter

# Or manual download
cd ~/development
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/macos/flutter_macos_3.22.0-stable.zip
unzip flutter_macos_3.22.0-stable.zip

# Add to PATH
export PATH="$PATH:$HOME/development/flutter/bin"

# Add to zshrc for persistence
echo 'export PATH="$PATH:$HOME/development/flutter/bin"' >> ~/.zshrc

# Verify installation
flutter doctor -v
```

**Linux Installation:**

```bash
# Download Flutter SDK
cd ~
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.0-stable.tar.xz
tar xf flutter_linux_3.22.0-stable.tar.xz

# Add to PATH
export PATH="$PATH:$HOME/flutter/bin"
echo 'export PATH="$PATH:$HOME/flutter/bin"' >> ~/.bashrc

# Verify
flutter doctor -v
```

### 1.3 Installing Android Studio & SDK

```bash
# Download Android Studio from https://developer.android.com/studio

# After installation, open Android Studio and go to:
# Configure > SDK Manager

# Install the following:
# - Android SDK Platform 33 (API 33)
# - Android SDK Platform 34 (API 34)
# - Android SDK Build-Tools 34.0.0
# - Android Emulator
# - Intel HAXM or AMD Hypervisor

# Accept licenses
flutter doctor --android-licenses
```

### 1.4 Creating Android Virtual Device (AVD)

```bash
# List available devices
avdmanager list device

# Create a new AVD
avdmanager create avd -n Pixel_6_API_33 -k "system-images;android-33;google_apis;x86_64" -d "pixel_6"

# Start emulator from command line
emulator -avd Pixel_6_API_33

# Or from Android Studio: Tools > AVD Manager > Run
```

### 1.5 iOS Setup (macOS only)

```bash
# Install Xcode from Mac App Store
# Open Xcode once to accept licenses

# Install CocoaPods
sudo gem install cocoapods

# Install iOS simulator
xcodebuild -downloadPlatform iOS

# Verify Flutter iOS setup
flutter doctor -v

# Open iOS simulator
open -a Simulator
```

### 1.6 Setting up Visual Studio Code / Android Studio

**VS Code Extensions to install:**
- Flutter (Dart) by Dart Code
- Flutter Riverpod Snippets
- Flutter Intl (i18n)
- Flutter Tree
- BLOC, Riverpod, GetX Snippets
- Error Lens
- GitLens
- Prettier
- Thunder Client (API testing)

**VS Code Settings (settings.json):**

```json
{
  "dart.flutterSdkPath": "~/development/flutter",
  "dart.lineLength": 120,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "files.associations": {
    "*.yaml": "yaml"
  },
  "[dart]": {
    "editor.tabSize": 2,
    "editor.rulers": [120]
  },
  "flutter.emulators": {
    "Pixel 6 API 33": {
      "id": "Pixel_6_API_33"
    }
  }
}
```

---

## Part 2: Project Initialization

### 2.1 Create New Flutter Project

```bash
# Create project with specific package name
flutter create --org com.yourcompany --project-name spotify_analytics spotify_analytics

# Navigate to project
cd spotify_analytics

# Enable desktop and web support (optional)
flutter config --enable-web
flutter config --enable-macos-desktop
flutter config --enable-windows-desktop
```

### 2.2 Complete pubspec.yaml Configuration

```yaml
name: spotify_analytics
description: Real-time Spotify Analytics with SignalR
version: 2.0.0+1
publish_to: none

environment:
  sdk: '>=3.0.0 <4.0.0'
  flutter: '>=3.22.0'

dependencies:
  flutter:
    sdk: flutter
  
  # Core
  cupertino_icons: ^1.0.6
  google_fonts: ^6.1.0
  
  # State Management
  riverpod: ^2.5.1
  flutter_riverpod: ^2.5.1
  riverpod_annotation: ^2.3.5
  
  # Networking
  dio: ^5.4.0
  retrofit: ^4.0.3
  logger: ^2.0.2
  signalr_core: ^1.2.3
  connectivity_plus: ^6.0.0
  
  # Storage
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  flutter_secure_storage: ^9.0.0
  path_provider: ^2.1.2
  
  # UI
  cached_network_image: ^3.3.1
  fl_chart: ^0.66.0
  lottie: ^3.0.0
  shimmer: ^3.0.0
  animated_text_kit: ^4.2.2
  
  # Audio
  just_audio: ^0.9.36
  audio_service: ^0.18.12
  audio_session: ^0.1.18
  
  # Utilities
  equatable: ^2.0.5
  intl: ^0.19.0
  share_plus: ^7.2.2
  url_launcher: ^6.2.5
  permission_handler: ^11.0.1

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0
  build_runner: ^2.4.8
  retrofit_generator: ^8.0.0
  riverpod_generator: ^2.4.0
  hive_generator: ^2.0.1

flutter:
  uses-material-design: true
  
  assets:
    - assets/animations/
    - assets/icons/
    - assets/images/
  
  fonts:
    - family: SpotifyCircular
      fonts:
        - asset: assets/fonts/CircularStd-Book.ttf
          weight: 400
        - asset: assets/fonts/CircularStd-Medium.ttf
          weight: 500
        - asset: assets/fonts/CircularStd-Bold.ttf
          weight: 700
        - asset: assets/fonts/CircularStd-Black.ttf
          weight: 900

# Add this for iOS deployment
flutter_ios:
  version: 2.0.0
  build_number: 1

# Add this for Android deployment
flutter_android:
  version_code: 1
  version_name: 2.0.0
```

### 2.3 Install Dependencies

```bash
# Clean and get packages
flutter clean
flutter pub get

# Generate code for Retrofit, Riverpod, Hive
flutter pub run build_runner build --delete-conflicting-outputs

# Verify no conflicts
flutter pub outdated
```

---

## Part 3: Spotify OAuth Configuration

### 3.1 Register Spotify Application

1. **Go to Spotify Developer Dashboard:** https://developer.spotify.com/dashboard
2. **Log in** with your Spotify account
3. **Click "Create App"**
4. **Fill in application details:**
   - App Name: `Spotify Analytics Pro`
   - App Description: `Real-time music analytics dashboard`
   - Redirect URIs: 
     - `spotify-analytics://oauth`
     - `http://localhost:64206/oauth-callback` (for web debug)
     - `https://api.yourdomain.com/auth/callback`
5. **Save Client ID and Client Secret**

### 3.2 Configure Android Deep Linking

**android/app/src/main/AndroidManifest.xml:**

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application>
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            
            <!-- OAuth Deep Link -->
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:scheme="spotify-analytics" android:host="oauth"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
```

### 3.3 Configure iOS Deep Linking

**ios/Runner/Info.plist:**

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>com.yourcompany.spotifyanalytics</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>spotify-analytics</string>
        </array>
    </dict>
</array>

<key>LSApplicationQueriesSchemes</key>
<array>
    <string>spotify</string>
</array>
```

### 3.4 OAuth Service Implementation

```dart
// lib/services/auth_service.dart
import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:dio/dio.dart';
import 'dart:convert';

class SpotifyAuthService {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();
  final Dio _dio = Dio();
  
  // Spotify OAuth configuration
  static const String clientId = 'YOUR_SPOTIFY_CLIENT_ID';
  static const String clientSecret = 'YOUR_SPOTIFY_CLIENT_SECRET';
  static const String redirectUri = 'spotify-analytics://oauth';
  static const String authUrl = 'https://accounts.spotify.com/authorize';
  static const String tokenUrl = 'https://accounts.spotify.com/api/token';
  
  static const List<String> scopes = [
    'user-read-private',
    'user-read-email',
    'user-read-currently-playing',
    'user-read-recently-played',
    'user-top-read',
    'user-modify-playback-state',
    'user-read-playback-state',
    'playlist-read-private',
    'playlist-modify-private',
    'playlist-modify-public',
    'user-follow-read',
    'user-library-read',
    'user-library-modify'
  ];
  
  Future<bool> authenticate() async {
    try {
      // Generate code verifier and challenge for PKCE
      final codeVerifier = _generateCodeVerifier();
      final codeChallenge = _generateCodeChallenge(codeVerifier);
      
      // Save code verifier for later
      await _storage.write(key: 'code_verifier', value: codeVerifier);
      
      // Build authorization URL
      final authUrlWithParams = Uri.parse(authUrl).replace(
        queryParameters: {
          'client_id': clientId,
          'response_type': 'code',
          'redirect_uri': redirectUri,
          'scope': scopes.join(' '),
          'code_challenge_method': 'S256',
          'code_challenge': codeChallenge,
          'show_dialog': 'true',
        },
      );
      
      // Open browser for authentication
      final result = await _openAuthBrowser(authUrlWithParams.toString());
      
      if (result != null && result.contains('code=')) {
        final code = _extractCode(result);
        final tokens = await _exchangeCodeForTokens(code, codeVerifier);
        
        if (tokens != null) {
          await _storage.write(key: 'access_token', value: tokens['access_token']);
          await _storage.write(key: 'refresh_token', value: tokens['refresh_token']);
          await _storage.write(key: 'expires_at', 
              value: (DateTime.now().millisecondsSinceEpoch + (tokens['expires_in'] * 1000)).toString());
          
          return true;
        }
      }
      
      return false;
    } catch (e) {
      debugPrint('Authentication error: $e');
      return false;
    }
  }
  
  String _generateCodeVerifier() {
    final random = Random.secure();
    final values = List<int>.generate(64, (_) => random.nextInt(256));
    return base64Url.encode(values).replaceAll('=', '');
  }
  
  String _generateCodeChallenge(String codeVerifier) {
    final bytes = utf8.encode(codeVerifier);
    final digest = sha256.convert(bytes);
    return base64Url.encode(digest.bytes).replaceAll('=', '');
  }
  
  Future<Map<String, dynamic>?> _exchangeCodeForTokens(String code, String codeVerifier) async {
    try {
      final response = await _dio.post(
        tokenUrl,
        data: {
          'client_id': clientId,
          'grant_type': 'authorization_code',
          'code': code,
          'redirect_uri': redirectUri,
          'code_verifier': codeVerifier,
        },
        options: Options(
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ${base64Encode(utf8.encode('$clientId:$clientSecret'))}',
          },
        ),
      );
      
      if (response.statusCode == 200) {
        return response.data;
      }
    } catch (e) {
      debugPrint('Token exchange error: $e');
    }
    return null;
  }
  
  Future<String?> refreshAccessToken() async {
    final refreshToken = await _storage.read(key: 'refresh_token');
    if (refreshToken == null) return null;
    
    try {
      final response = await _dio.post(
        '/api/auth/refresh',
        data: {'refresh_token': refreshToken},
      );
      
      if (response.statusCode == 200) {
        final newToken = response.data['access_token'];
        await _storage.write(key: 'access_token', value: newToken);
        return newToken;
      }
    } catch (e) {
      debugPrint('Token refresh error: $e');
    }
    return null;
  }
}
```

---

## Part 4: Environment Configuration

### 4.1 Create Environment Files

**.env.dev (Development):**

```env
API_BASE_URL=https://dev-api.yourdomain.com
WS_BASE_URL=wss://dev-api.yourdomain.com
SENTRY_DSN=https://dev.sentry.io/12345
ENVIRONMENT=development
ENABLE_LOGS=true
CACHE_DURATION=60
```

**.env.staging:**

```env
API_BASE_URL=https://staging-api.yourdomain.com
WS_BASE_URL=wss://staging-api.yourdomain.com
SENTRY_DSN=https://staging.sentry.io/12345
ENVIRONMENT=staging
ENABLE_LOGS=true
CACHE_DURATION=300
```

**.env.production:**

```env
API_BASE_URL=https://api.yourdomain.com
WS_BASE_URL=wss://api.yourdomain.com
SENTRY_DSN=https://prod.sentry.io/12345
ENVIRONMENT=production
ENABLE_LOGS=false
CACHE_DURATION=3600
```

### 4.2 Environment Loader

```dart
// lib/utils/environment.dart
import 'package:flutter/foundation.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class EnvironmentConfig {
  static const String dev = 'development';
  static const String staging = 'staging';
  static const String prod = 'production';
  
  static late final String currentEnvironment;
  static late final String apiBaseUrl;
  static late final String wsBaseUrl;
  static late final String sentryDsn;
  static late final bool enableLogs;
  static late final int cacheDuration;
  
  static Future<void> load() async {
    currentEnvironment = const String.fromEnvironment('ENVIRONMENT', defaultValue: dev);
    
    switch (currentEnvironment) {
      case dev:
        await dotenv.load(fileName: '.env.dev');
        break;
      case staging:
        await dotenv.load(fileName: '.env.staging');
        break;
      case prod:
        await dotenv.load(fileName: '.env.production');
        break;
    }
    
    apiBaseUrl = dotenv.get('API_BASE_URL');
    wsBaseUrl = dotenv.get('WS_BASE_URL');
    sentryDsn = dotenv.get('SENTRY_DSN');
    enableLogs = dotenv.get('ENABLE_LOGS') == 'true';
    cacheDuration = int.parse(dotenv.get('CACHE_DURATION'));
  }
}
```

---

## Part 5: Running the Application

### 5.1 Run on Android Emulator

```bash
# List available emulators
flutter emulators

# Launch emulator
flutter emulators --launch Pixel_6_API_33

# Run app on emulator
flutter run -d emulator-5554 --flavor development

# Or run with specific build mode
flutter run --debug --flavor development
flutter run --release --flavor production
```

### 5.2 Run on iOS Simulator (macOS)

```bash
# Open iOS simulator
open -a Simulator

# Run on iOS
flutter run -d "iPhone 15 Pro"

# For specific iOS version
flutter run --device-id "iPhone 15 Pro (iOS 17.0)"
```

### 5.3 Run on Physical Device

**Android:**
```bash
# Enable Developer options and USB debugging on phone
# Connect via USB

# Check connected devices
adb devices

# Run on physical device
flutter run -d <device_id>
```

**iOS:**
```bash
# Connect iPhone via USB
# Trust computer on device

# Run on physical device (requires Apple Developer account)
flutter run -d "iPhone"
```

### 5.4 Build Release APK

```bash
# Build APK for development
flutter build apk --flavor development --debug

# Build release APK
flutter build apk --flavor production --release --split-per-abi

# Build App Bundle for Google Play
flutter build appbundle --flavor production --release

# Output locations:
# build/app/outputs/flutter-apk/app-release.apk
# build/app/outputs/bundle/release/app-release.aab
```

### 5.5 Build iOS Archive

```bash
# Build for iOS (requires macOS)
flutter build ios --flavor production --release

# Then open in Xcode
open ios/Runner.xcworkspace

# In Xcode: Product > Archive
```

---

## Part 6: Testing Configuration

### 6.1 Unit Tests Setup

```dart
// test/unit/models/track_model_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:spotify_analytics/models/track_model.dart';

void main() {
  group('Track Model Tests', () {
    test('Track.fromJson creates correct object', () {
      final json = {
        'id': '123',
        'name': 'Test Track',
        'artist': 'Test Artist',
        'albumArtUrl': 'https://example.com/image.jpg',
        'durationMs': 180000,
        'isPlaying': true,
        'playedAt': DateTime.now().toIso8601String(),
      };
      
      final track = Track.fromJson(json);
      
      expect(track.id, '123');
      expect(track.name, 'Test Track');
      expect(track.artist, 'Test Artist');
    });
  });
}
```

### 6.2 Widget Tests Setup

```dart
// test/widgets/home_screen_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:spotify_analytics/screens/home/home_screen.dart';

void main() {
  testWidgets('Home screen renders correctly', (tester) async {
    await tester.pumpWidget(
      const ProviderScope(
        child: MaterialApp(
          home: HomeScreen(),
        ),
      ),
    );
    
    expect(find.text('Home'), findsOneWidget);
  });
}
```

### 6.3 Integration Tests Setup

```dart
// integration_test/app_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:spotify_analytics/main.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  
  testWidgets('Full app flow test', (tester) async {
    await tester.pumpWidget(const MyApp());
    await tester.pumpAndSettle();
    
    // Test authentication flow
    expect(find.text('Connect to Spotify'), findsOneWidget);
    
    // Tap login button
    await tester.tap(find.text('Continue with Spotify'));
    await tester.pumpAndSettle();
  });
}
```

### 6.4 Run Tests

```bash
# Run unit tests
flutter test test/unit/

# Run widget tests
flutter test test/widgets/

# Run integration tests
flutter test integration_test/

# Run tests with coverage
flutter test --coverage

# Generate coverage report
genhtml coverage/lcov.info -o coverage/html
```

---

## Part 7: Azure Deployment

### 7.1 Create Azure App Service for API Backend

```bash
# Install Azure CLI
# Windows: winget install Microsoft.AzureCLI
# macOS: brew install azure-cli
# Linux: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login to Azure
az login

# Create resource group
az group create --name SpotifyAnalyticsRG --location eastus

# Create App Service Plan (Linux)
az appservice plan create \
  --name SpotifyPlan \
  --resource-group SpotifyAnalyticsRG \
  --sku P1V3 \
  --is-linux \
  --location eastus

# Create Web App for .NET 10 API
az webapp create \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --plan SpotifyPlan \
  --runtime "DOTNET:10.0"
```

### 7.2 Configure Azure App Service Settings

```bash
# Set environment variables
az webapp config appsettings set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --settings \
    ASPNETCORE_ENVIRONMENT=Production \
    Jwt__Key="your-jwt-key-minimum-32-characters" \
    ConnectionStrings__PostgreSQL="Host=spotify-db.postgres.database.azure.com;Database=spotify_db;Username=spotify@spotify-db;Password=YourPassword" \
    ConnectionStrings__Redis="spotify-cache.redis.cache.windows.net:6380,password=YourPassword,ssl=True,abortConnect=False"

# Enable WebSockets (required for SignalR)
az webapp config set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --web-sockets-enabled true

# Set Always On (prevents app from going idle)
az webapp config set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --always-on true

# Set HTTP version to 2.0 for better performance
az webapp config set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --http20-enabled true
```

### 7.3 Create Azure PostgreSQL Database

```bash
# Create PostgreSQL server
az postgres flexible-server create \
  --name spotify-db \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --admin-user spotifyadmin \
  --admin-password YourSecurePassword123! \
  --sku-name Standard_B1ms \
  --tier Burstable \
  --version 16 \
  --storage-size 32

# Create database
az postgres flexible-server db create \
  --server-name spotify-db \
  --resource-group SpotifyAnalyticsRG \
  --database-name spotify_db

# Configure firewall rules for Azure services
az postgres flexible-server firewall-rule create \
  --server-name spotify-db \
  --resource-group SpotifyAnalyticsRG \
  --name AllowAllAzureIPs \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0
```

### 7.4 Create Azure Redis Cache for SignalR Backplane

```bash
# Create Redis Cache
az redis create \
  --name spotify-cache \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --sku Basic \
  --vm-size C0 \
  --enable-non-ssl-port false

# Get Redis connection string
az redis show \
  --name spotify-cache \
  --resource-group SpotifyAnalyticsRG \
  --query "sslPort" \
  --output tsv
```

### 7.5 Create Azure Storage Account for Assets

```bash
# Create storage account
az storage account create \
  --name spotifystorageacc \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2

# Create blob container for album art cache
az storage container create \
  --name album-art-cache \
  --account-name spotifystorageacc \
  --public-access blob

# Get connection string
az storage account show-connection-string \
  --name spotifystorageacc \
  --resource-group SpotifyAnalyticsRG \
  --output tsv
```

### 7.6 Deploy Flutter App to Azure Static Web Apps

```bash
# Build Flutter web version
flutter build web --release --base-href "/"

# Install Static Web Apps CLI
npm install -g @azure/static-web-apps-cli

# Deploy to Azure Static Web Apps
swa deploy \
  --deployment-token YOUR_DEPLOYMENT_TOKEN \
  --app-artifact-location ./build/web \
  --env production

# Or use Azure CLI
az staticwebapp create \
  --name spotify-flutter-app \
  --resource-group SpotifyAnalyticsRG \
  --source ./build/web \
  --location eastus \
  --sku Standard \
  --app-artifact-location "build/web"
```

### 7.7 GitHub Actions CI/CD Pipeline

**.github/workflows/flutter-ci.yml:**

```yaml
name: Flutter CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build-and-deploy-android:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.22.0'
          channel: 'stable'
          
      - name: Install dependencies
        run: flutter pub get
        
      - name: Run tests
        run: flutter test
        
      - name: Build APK
        run: flutter build apk --release --split-per-abi
        
      - name: Upload APK to Azure
        uses: azure/CLI@v1
        with:
          inlineScript: |
            az storage blob upload-batch \
              --account-name spotifystorageacc \
              --source build/app/outputs/flutter-apk \
              --destination apk-releases \
              --overwrite
              
      - name: Deploy to App Center
        run: |
          appcenter distribute release \
            --app "your-app-center-app" \
            --group "Testers" \
            --file "build/app/outputs/flutter-apk/app-release.apk"

  deploy-to-azure:
    runs-on: ubuntu-latest
    needs: build-and-deploy-android
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v4
      
      - name: 'Login to Azure'
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
          
      - name: 'Deploy to Azure Web App'
        uses: azure/webapps-deploy@v2
        with:
          app-name: 'spotify-api-prod'
          slot-name: 'production'
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
```

**.github/workflows/dotnet-ci.yml:**

```yaml
name: .NET 10 API CI/CD

on:
  push:
    branches: [main, develop]
    paths:
      - 'backend/**'
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup .NET 10
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '10.0.x'
          
      - name: Restore dependencies
        run: dotnet restore
        
      - name: Build
        run: dotnet build --no-restore
        
      - name: Run tests
        run: dotnet test --no-build --verbosity normal
        
      - name: Publish with NativeAOT
        run: dotnet publish -c Release -r linux-x64 --self-contained true -p:PublishSingleFile=true -p:PublishTrimmed=true -o ./publish
        
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: api-artifact
          path: ./publish
          
  deploy-to-azure:
    runs-on: ubuntu-latest
    needs: build-and-test
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: api-artifact
          path: ./publish
          
      - name: 'Login to Azure'
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
          
      - name: 'Deploy to Azure Web App'
        uses: azure/webapps-deploy@v2
        with:
          app-name: 'spotify-api-prod'
          slot-name: 'production'
          package: ./publish
```

### 7.8 Configure Azure Application Insights

```bash
# Create Application Insights
az monitor app-insights component create \
  --app spotify-analytics-insights \
  --resource-group SpotifyAnalyticsRG \
  --location eastus \
  --application-type web

# Get instrumentation key
az monitor app-insights component show \
  --app spotify-analytics-insights \
  --resource-group SpotifyAnalyticsRG \
  --query "instrumentationKey"

# Add to app settings
az webapp config appsettings set \
  --name spotify-api-prod \
  --resource-group SpotifyAnalyticsRG \
  --settings \
    APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=your-key;IngestionEndpoint=https://eastus-1.in.applicationinsights.azure.com/"
```

### 7.9 Setup Azure Front Door for Global Distribution

```bash
# Create Front Door profile
az afd profile create \
  --profile-name spotify-frontdoor \
  --resource-group SpotifyAnalyticsRG \
  --sku Premium_AzureFrontDoor

# Create endpoint
az afd endpoint create \
  --resource-group SpotifyAnalyticsRG \
  --profile-name spotify-frontdoor \
  --endpoint-name spotify-global

# Create origin group
az afd origin-group create \
  --resource-group SpotifyAnalyticsRG \
  --profile-name spotify-frontdoor \
  --origin-group-name api-origin-group

# Add origin
az afd origin create \
  --resource-group SpotifyAnalyticsRG \
  --profile-name spotify-frontdoor \
  --origin-group-name api-origin-group \
  --origin-name spotify-api-origin \
  --host-name spotify-api-prod.azurewebsites.net
```

### 7.10 Monitoring & Alerts

```bash
# Create metric alert for CPU usage
az monitor metrics alert create \
  --name "High CPU Usage" \
  --resource-group SpotifyAnalyticsRG \
  --scopes "/subscriptions/your-subscription/resourceGroups/SpotifyAnalyticsRG/providers/Microsoft.Web/sites/spotify-api-prod" \
  --condition "avg Percentage CPU > 80" \
  --description "Alert when CPU exceeds 80%" \
  --evaluation-frequency 5m \
  --window-size 15m \
  --severity 2

# Create alert for 5xx errors
az monitor metrics alert create \
  --name "High Error Rate" \
  --resource-group SpotifyAnalyticsRG \
  --scopes "/subscriptions/your-subscription/resourceGroups/SpotifyAnalyticsRG/providers/Microsoft.Web/sites/spotify-api-prod" \
  --condition "count Http5xx > 10" \
  --description "Alert when 5xx errors exceed 10 in 5 minutes" \
  --evaluation-frequency 5m \
  --window-size 5m \
  --severity 1
```

---

## Part 8: Troubleshooting Guide

### 8.1 Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **SignalR connection fails** | Check WebSocket support: `az webapp config set --web-sockets-enabled true` |
| **Android build fails** | Run `flutter clean` and `flutter pub get`, then rebuild |
| **iOS build fails** | `cd ios && pod repo update && pod install && cd ..` |
| **OAuth redirect not working** | Verify deep link configuration in AndroidManifest.xml and Info.plist |
| **Rate limiting errors** | Implement exponential backoff in API calls |

### 8.2 Debugging Commands

```bash
# Check SignalR connection health
curl -X GET https://api.yourdomain.com/health

# Monitor logs in real-time
az webapp log tail --name spotify-api-prod --resource-group SpotifyAnalyticsRG

# Check WebSocket connections
az webapp config show --name spotify-api-prod --resource-group SpotifyAnalyticsRG --query "webSocketsEnabled"

# View application logs
flutter logs

# Check device logs
adb logcat | grep flutter
```

### 8.3 Performance Optimization Checklist

```bash
# Enable HTTP/2
az webapp config set --http20-enabled true

# Enable Always On
az webapp config set --always-on true

# Increase instance count for scale
az appservice plan update --name SpotifyPlan --resource-group SpotifyAnalyticsRG --number-of-workers 3

# Enable Application Insights for performance monitoring
az webapp config appsettings set --settings APPINSIGHTS_INSTRUMENTATIONKEY=your-key

# Configure auto-healing
az webapp config set --auto-heal-enabled true
```

---

## Part 9: Production Readiness Checklist

- [ ] All environment variables configured in Azure App Settings
- [ ] SSL/TLS certificates configured (Azure provides automatically)
- [ ] Custom domain configured: `az webapp config hostname add`
- [ ] CDN enabled for static assets
- [ ] Database backups configured
- [ ] Redis cache persistence enabled
- [ ] Application Insights monitoring active
- [ ] Alerts configured for critical metrics
- [ ] Load testing completed with k6 or JMeter
- [ ] Security scanning passed
- [ ] Privacy policy and terms of service implemented
- [ ] App store compliance checked (Apple Music guidelines)
- [ ] Crash reporting (Sentry or Firebase Crashlytics) configured
- [ ] Analytics tracking (Mixpanel or Segment) implemented
- [ ] Feature flags configured for gradual rollouts

---

## Next Steps

This development environment setup works with the backend described in **"Dev Setup: SignalR with .NET 10 API - Spotify Clone With Flutter And .NET 10"**. For complete backend setup including PostgreSQL, Redis, and Azure deployment, continue to the companion guide.

**Quick Reference:**

| Command | Purpose |
|---------|---------|
| `flutter run -d chrome` | Run in Chrome for web debugging |
| `flutter build apk --release` | Build production APK |
| `flutter build ios --release` | Build iOS archive |
| `az webapp deploy` | Deploy to Azure |
| `flutter test --coverage` | Run tests with coverage |

**Support Resources:**
- Flutter Documentation: https://docs.flutter.dev
- Azure SDK: https://azure.github.io/azure-sdk/
- SignalR Documentation: https://learn.microsoft.com/en-us/aspnet/signalr/

---

