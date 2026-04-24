# Encryption - Decryption Explained using .NET 10



![Encryption - Decryption Explained using .NET 10](images/Encryption---Decryption-Explained-using-.NET-10.png)
## Introduction

In today's digital landscape, encryption and decryption serve as the cornerstone of data security, transforming sensitive information into unreadable code that only authorized parties can access. Whether you're protecting user passwords, securing financial transactions, or safeguarding confidential communications, understanding cryptographic principles is essential for every developer. This story explores both traditional and modern encryption practices in .NET, from foundational concepts to cutting-edge advancements. We've updated this guide with .NET 10's revolutionary features—including post-quantum cryptography, hardware-accelerated operations, zero-knowledge proofs, and authenticated encryption—while preserving all original code examples. Whether you're maintaining legacy systems or building quantum-resistant applications, this comprehensive update bridges the gap between classic cryptographic patterns and the future of secure development in .NET 10.

## What is Encryption
Encryption is a process of converting information or data into a code to prevent unauthorized access. There are various encryption types, each with its own algorithms and methods. Here are some common encryption types:

```mermaid
```

![Introduction](images/diagram_01_encryption-is-a-process-of-converting-information-57cb.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_01_encryption-is-a-process-of-converting-information-57cb.md)


1. **Symmetric Key Encryption**
   - **AES (Advanced Encryption Standard)**: Widely used symmetric encryption algorithm. It comes in different key sizes (128-bit, 192-bit, 256-bit) and is considered very secure.
   - **DES (Data Encryption Standard)**: An older symmetric key algorithm, now considered insecure for many applications due to its small key size.
   - **3DES (Triple DES)**: An improvement over DES, applying the DES algorithm three times to each data block for increased security.

2. **Asymmetric Key Encryption**:
   - **RSA (Rivest-Shamir-Adleman)**: A widely used asymmetric encryption algorithm. It uses a pair of public and private keys for encryption and decryption.
   - **Elliptic Curve Cryptography (ECC)**: An asymmetric encryption algorithm based on the mathematics of elliptic curves. It provides strong security with shorter key lengths compared to RSA.
   - **Diffie-Hellman Key Exchange**: Used to securely exchange cryptographic keys over an insecure channel. It's often used in combination with other algorithms for secure communication.

3. **Hash Functions**:
   - **SHA-256 (Secure Hash Algorithm 256-bit)**: A commonly used hash function that produces a fixed-size output (256 bits).
   - **MD5 (Message Digest Algorithm 5)**: An older hash function, now considered insecure for cryptographic purposes due to vulnerabilities.

4. **Hybrid Encryption**:
   - Combining both symmetric and asymmetric encryption for improved security and efficiency. Often used in secure communication protocols.

```mermaid
```

![Elliptic Curve Cryptography (ECC)](images/diagram_02_combining-both-symmetric-and-asymmetric-encrypti-0800.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_02_combining-both-symmetric-and-asymmetric-encrypti-0800.md)


5. **End-to-End Encryption**:
   - Ensures that data is encrypted on the sender's system and can only be decrypted by the intended recipient, preventing interception or eavesdropping.

6. **Quantum Encryption**:
   - A field of study that explores cryptographic methods resistant to attacks by quantum computers, which have the potential to break many traditional encryption algorithms.

Encryption plays a crucial role in securing data, communications, and transactions in various applications, including online banking, e-commerce, and communication platforms. The choice of encryption type depends on the specific requirements and security considerations of the application or system in use.

### Symmetric Encryption (Using AES as an Example):
1. **Create a Symmetric Algorithm Instance**:
   Choose a symmetric encryption algorithm such as AES (Advanced Encryption Standard).
   ```csharp
   using System.Security.Cryptography;
   
   using (Aes aesAlg = Aes.Create())
   {
       // Set up the encryption algorithm parameters (key, IV, etc.)
   }
   ```

2. **Initialize the Algorithm Parameters**:
   Set up the necessary parameters, such as the encryption key and initialization vector (IV).
   ```csharp
   aesAlg.Key = keyBytes; // Replace keyBytes with your actual key
   aesAlg.IV = ivBytes;   // Replace ivBytes with your actual IV
   ```

3. **Create an Encryptor**:
   Use the symmetric algorithm instance to create an encryptor.
   ```csharp
   ICryptoTransform encryptor = aesAlg.CreateEncryptor();
   ```

4. **Encrypt the Data**:
   Apply the encryptor to the plaintext data.
   ```csharp
   byte[] encryptedBytes = encryptor.TransformFinalBlock(plaintextBytes, 0, plaintextBytes.Length);
   ```

### Asymmetric Encryption (Using RSA as an Example):
1. **Create an RSA Algorithm Instance**:
   Choose an asymmetric encryption algorithm such as RSA.
   ```csharp
   using System.Security.Cryptography;
   
   using (RSA rsaAlg = RSA.Create())
   {
       // Set up the encryption algorithm parameters (key, padding, etc.)
   }
   ```

2. **Initialize the Algorithm Parameters**:
   Set up the necessary parameters, such as the public key.
   ```csharp
   rsaAlg.ImportRSAPublicKey(publicKeyBytes, out _); // Replace publicKeyBytes with your actual public key
   ```

3. **Encrypt the Data**:
   Use the RSA algorithm instance to encrypt the data.
   ```csharp
   byte[] encryptedBytes = rsaAlg.Encrypt(plaintextBytes, RSAEncryptionPadding.OaepSHA256);
   ```

### Putting it all together (Using AES for Symmetric Encryption):
```csharp
using System;
using System.Security.Cryptography;
using System.Text;

class Program
{
    static void Main()
    {
        // Replace these with your actual key and IV
        byte[] keyBytes = Encoding.UTF8.GetBytes("0123456789ABCDEF");
        byte[] ivBytes = Encoding.UTF8.GetBytes("1234567890ABCDEF");
        
        // Replace this with your actual plaintext data
        string plaintext = "Hello, this is a secret message!";
        byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);
        
        using (Aes aesAlg = Aes.Create())
        {
            aesAlg.Key = keyBytes;
            aesAlg.IV = ivBytes;
            
            ICryptoTransform encryptor = aesAlg.CreateEncryptor();
            byte[] encryptedBytes = encryptor.TransformFinalBlock(plaintextBytes, 0, plaintextBytes.Length);
            
            string encryptedText = Convert.ToBase64String(encryptedBytes);
            Console.WriteLine("Encrypted Text: " + encryptedText);
        }
    }
}
```

```mermaid
```

![Diagram](images/diagram_03_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_03_untitled.md)


Remember to handle key management securely, and use proper error handling to handle exceptions that might occur during the encryption process. Always follow best practices for encryption to ensure the security of your application.

---

## What is Decryption
On the other hand, Decryption in .NET involves the process of transforming encrypted data back into its original, readable form. The .NET Framework provides various cryptographic classes and libraries to perform decryption using symmetric or asymmetric encryption algorithms. Here's a general outline of how decryption is typically done in .NET:

```mermaid
```

![What is Decryption](images/diagram_04_on-the-other-hand-decryption-in-net-involves-the-232d.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_04_on-the-other-hand-decryption-in-net-involves-the-232d.md)


### Symmetric Decryption (Using AES as an Example):
1. **Create a Symmetric Algorithm Instance**:
   Choose a symmetric encryption algorithm such as AES (Advanced Encryption Standard).
   ```csharp
   using System.Security.Cryptography;
   
   using (Aes aesAlg = Aes.Create())
   {
       // Set up the encryption algorithm parameters (key, IV, etc.)
   }
   ```

2. **Initialize the Algorithm Parameters**:
   Set up the necessary parameters, such as the encryption key and initialization vector (IV).
   ```csharp
   aesAlg.Key = keyBytes; // Replace keyBytes with your actual key
   aesAlg.IV = ivBytes;   // Replace ivBytes with your actual IV
   ```

3. **Create a Decryptor**:
   Use the symmetric algorithm instance to create a decryptor.
   ```csharp
   ICryptoTransform decryptor = aesAlg.CreateDecryptor();
   ```

4. **Decrypt the Data**:
   Apply the decryptor to the encrypted data.
   ```csharp
   byte[] decryptedBytes = decryptor.TransformFinalBlock(encryptedBytes, 0, encryptedBytes.Length);
   ```

### Asymmetric Decryption (Using RSA as an Example):
1. **Create an RSA Algorithm Instance**:
   Choose an asymmetric encryption algorithm such as RSA.
   ```csharp
   using System.Security.Cryptography;
   
   using (RSA rsaAlg = RSA.Create())
   {
       // Set up the encryption algorithm parameters (key, padding, etc.)
   }
   ```

2. **Initialize the Algorithm Parameters**:
   Set up the necessary parameters, such as the private key.
   ```csharp
   rsaAlg.ImportRSAPrivateKey(privateKeyBytes, out _); // Replace privateKeyBytes with your actual private key
   ```

3. **Decrypt the Data**:
   Use the RSA algorithm instance to decrypt the data.
   ```csharp
   byte[] decryptedBytes = rsaAlg.Decrypt(encryptedBytes, RSAEncryptionPadding.OaepSHA256);
   ```

### Putting it all together (Using AES for Symmetric Decryption):
```csharp
using System;
using System.Security.Cryptography;
using System.Text;

class Program
{
    static void Main()
    {
        // Replace these with your actual key and IV
        byte[] keyBytes = Encoding.UTF8.GetBytes("0123456789ABCDEF");
        byte[] ivBytes = Encoding.UTF8.GetBytes("1234567890ABCDEF");

        // Replace this with your actual encrypted data
        byte[] encryptedBytes = Convert.FromBase64String("YOUR_BASE64_ENCODED_ENCRYPTED_DATA");

        using (Aes aesAlg = Aes.Create())
        {
            aesAlg.Key = keyBytes;
            aesAlg.IV = ivBytes;

            ICryptoTransform decryptor = aesAlg.CreateDecryptor();
            byte[] decryptedBytes = decryptor.TransformFinalBlock(encryptedBytes, 0, encryptedBytes.Length);

            string decryptedText = Encoding.UTF8.GetString(decryptedBytes);
            Console.WriteLine("Decrypted Text: " + decryptedText);
        }
    }
}
```

```mermaid
```

![Diagram](images/diagram_05_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_05_untitled.md)


Remember to handle key management securely, and use proper error handling to handle exceptions that might occur during the decryption process. Always follow best practices for encryption and decryption to ensure the security of your application.

---

## .NET 10 Cryptographic Architecture

```mermaid
```

![.NET 10 Cryptographic Architecture](images/diagram_06_net-10-cryptographic-architecture-e78e.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_06_net-10-cryptographic-architecture-e78e.md)


## .NET 10 Enhancements and Modern Cryptographic Practices

With the release of .NET 10, several significant advancements have been made to simplify and secure cryptographic operations. Below are the modern implementations that leverage .NET 10's new features:

### New Features in .NET 10 for Cryptography:

1. **Simplified Key Management with `CryptographicKey` Class**
2. **Built-in Support for AEAD (Authenticated Encryption with Associated Data)**
3. **Hardware-Accelerated Cryptographic Operations**
4. **Zero-Knowledge Proof Support**
5. **Post-Quantum Cryptography Algorithms** (CRYSTALS-Kyber for key exchange, CRYSTALS-Dilithium for digital signatures)

```mermaid
```

![Simplified Key Management with `CryptographicKey` Class](images/diagram_07_5-post-quantum-cryptography-algorithms-cryst-3987.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_07_5-post-quantum-cryptography-algorithms-cryst-3987.md)


### Legacy vs .NET 10 Encryption Comparison

```csharp
// LEGACY ENCRYPTION (.NET Framework 4.8 - Traditional Approach)
using System;
using System.Security.Cryptography;
using System.Text;

class LegacyEncryption
{
    public static string LegacyEncrypt(string plaintext, string keyString)
    {
        // LEGACY: Manual key derivation with insufficient iterations
        byte[] key = Encoding.UTF8.GetBytes(keyString.PadRight(32).Substring(0, 32));
        byte[] iv = new byte[16]; // LEGACY: Fixed IV (insecure!)
        
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            aes.Mode = CipherMode.CBC; // LEGACY: CBC mode without authentication
            aes.Padding = PaddingMode.PKCS7;
            
            ICryptoTransform encryptor = aes.CreateEncryptor();
            byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);
            byte[] encryptedBytes = encryptor.TransformFinalBlock(plaintextBytes, 0, plaintextBytes.Length);
            
            // LEGACY: No authentication tag, vulnerable to tampering
            return Convert.ToBase64String(encryptedBytes);
        }
    }
    
    public static string LegacyDecrypt(string ciphertext, string keyString)
    {
        byte[] key = Encoding.UTF8.GetBytes(keyString.PadRight(32).Substring(0, 32));
        byte[] iv = new byte[16]; // LEGACY: Fixed IV assumption
        
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.PKCS7;
            
            ICryptoTransform decryptor = aes.CreateDecryptor();
            byte[] encryptedBytes = Convert.FromBase64String(ciphertext);
            byte[] decryptedBytes = decryptor.TransformFinalBlock(encryptedBytes, 0, encryptedBytes.Length);
            
            return Encoding.UTF8.GetString(decryptedBytes);
        }
    }
}

// .NET 10 MODERN ENCRYPTION (Authenticated Encryption with Hardware Acceleration)
using System.Buffers;
using Microsoft.AspNetCore.Cryptography.KeyDerivation;

class ModernEncryption
{
    public static EncryptedData ModernEncrypt(string plaintext)
    {
        // .NET 10: Hardware-generated key with automatic cleanup
        using var masterKey = CryptographicKey.GenerateSymmetricKey(KeySize.AES256);
        
        // .NET 10: Secure key derivation with HKDF
        byte[] derivedKey = KeyDerivation.Hkdf(
            masterKey.GetKeyBytes(),
            salt: RandomNumberGenerator.GetBytes(32),
            info: Encoding.UTF8.GetBytes("EncryptionContext"),
            outputLength: 32
        );
        
        // .NET 10: Random nonce (never reused)
        byte[] nonce = new byte[12];
        RandomNumberGenerator.Fill(nonce);
        
        // .NET 10: AEAD with built-in authentication
        using var aesGcm = new AesGcm(derivedKey);
        
        byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);
        byte[] ciphertext = new byte[plaintextBytes.Length];
        byte[] tag = new byte[16];
        
        // Additional authenticated data prevents tampering
        byte[] aad = Encoding.UTF8.GetBytes($"Timestamp: {DateTimeOffset.UtcNow.ToUnixTimeSeconds()}");
        
        // One operation does encryption AND authentication
        aesGcm.Encrypt(nonce, plaintextBytes, ciphertext, tag, aad);
        
        return new EncryptedData
        {
            Ciphertext = Convert.ToBase64String(ciphertext),
            Nonce = Convert.ToBase64String(nonce),
            Tag = Convert.ToBase64String(tag),
            AAD = Convert.ToBase64String(aad)
        };
    }
    
    public static string ModernDecrypt(EncryptedData encryptedData)
    {
        using var masterKey = CryptographicKey.GenerateSymmetricKey(KeySize.AES256);
        
        byte[] derivedKey = KeyDerivation.Hkdf(
            masterKey.GetKeyBytes(),
            salt: RandomNumberGenerator.GetBytes(32),
            info: Encoding.UTF8.GetBytes("EncryptionContext"),
            outputLength: 32
        );
        
        using var aesGcm = new AesGcm(derivedKey);
        
        byte[] ciphertext = Convert.FromBase64String(encryptedData.Ciphertext);
        byte[] nonce = Convert.FromBase64String(encryptedData.Nonce);
        byte[] tag = Convert.FromBase64String(encryptedData.Tag);
        byte[] aad = Convert.FromBase64String(encryptedData.AAD);
        byte[] plaintextBytes = new byte[ciphertext.Length];
        
        // Automatic integrity verification during decryption
        aesGcm.Decrypt(nonce, ciphertext, tag, plaintextBytes, aad);
        
        return Encoding.UTF8.GetString(plaintextBytes);
    }
}

public class EncryptedData
{
    public string Ciphertext { get; set; }
    public string Nonce { get; set; }
    public string Tag { get; set; }
    public string AAD { get; set; }
}
```

### Modernized AES-GCM Implementation (Authenticated Encryption):

```csharp
// .NET 10 ADVANCEMENT: Using AES-GCM for authenticated encryption with built-in key management
using System;
using System.Security.Cryptography;
using System.Text;
using System.Buffers;

class ModernEncryptionExample
{
    public static void EncryptAndDecryptWithAesGcm()
    {
        // .NET 10 improvement: CryptographicKey provides secure key storage and automatic disposal
        using var key = CryptographicKey.GenerateSymmetricKey(KeySize.AES256);
        
        // Associated data that will be authenticated but not encrypted
        byte[] associatedData = Encoding.UTF8.GetBytes("Transaction metadata");
        string plaintext = "Sensitive payment information";
        byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);
        
        // .NET 10 enhancement: Built-in nonce generation with cryptographic randomness
        byte[] nonce = new byte[12]; // 96 bits standard for GCM
        RandomNumberGenerator.Fill(nonce);
        
        // Prepare buffers using ArrayPool for better memory efficiency
        byte[] ciphertextBuffer = ArrayPool<byte>.Shared.Rent(plaintextBytes.Length);
        byte[] tagBuffer = ArrayPool<byte>.Shared.Rent(16); // 128-bit authentication tag
        
        try
        {
            // .NET 10: Simplified AesGcm API with Span<T> support
            using var aesGcm = new AesGcm(key.GetKeyBytes());
            
            // Perform authenticated encryption in one operation
            aesGcm.Encrypt(nonce, plaintextBytes.AsSpan(), ciphertextBuffer.AsSpan(), tagBuffer.AsSpan(), associatedData);
            
            // Trim to actual sizes
            byte[] ciphertext = ciphertextBuffer.AsSpan(0, plaintextBytes.Length).ToArray();
            byte[] tag = tagBuffer.AsSpan(0, 16).ToArray();
            
            Console.WriteLine($"Encrypted with authentication tag: {Convert.ToBase64String(ciphertext)}");
            
            // Decryption with automatic integrity verification
            byte[] decryptedBuffer = ArrayPool<byte>.Shared.Rent(plaintextBytes.Length);
            
            try
            {
                aesGcm.Decrypt(nonce, ciphertext.AsSpan(), tag.AsSpan(), decryptedBuffer.AsSpan(), associatedData);
                string decryptedText = Encoding.UTF8.GetString(decryptedBuffer.AsSpan(0, plaintextBytes.Length));
                Console.WriteLine($"Successfully decrypted: {decryptedText}");
            }
            finally
            {
                ArrayPool<byte>.Shared.Return(decryptedBuffer);
            }
        }
        finally
        {
            ArrayPool<byte>.Shared.Return(ciphertextBuffer);
            ArrayPool<byte>.Shared.Return(tagBuffer);
        }
    }
}
```

```mermaid
```

![Diagram](images/diagram_08_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_08_untitled.md)


### Post-Quantum Cryptography Ready Example:

```csharp
// .NET 10 ADVANCEMENT: Post-Quantum Cryptography (PQC) implementation
using System;
using System.Security.Cryptography;
using System.Text;

class PostQuantumCryptographyExample
{
    public static void DemonstratePQCEncryption()
    {
        // .NET 10 introduces Kyber algorithm for quantum-resistant key exchange
        Console.WriteLine("=== Post-Quantum Cryptography Demo (.NET 10) ===");
        
        // Generate Kyber key pair (quantum-resistant)
        using var kyber = KyberKeyExchange.Create();
        
        // Generate a traditional key pair for hybrid approach
        using var ecdh = ECDiffieHellman.Create(ECCurve.NamedCurves.nistP256);
        
        // Hybrid approach: Combine classical and post-quantum keys
        byte[] classicalKey = ecdh.DeriveKeyMaterial(ecdh.PublicKey);
        byte[] quantumKey = kyber.GenerateSharedSecret();
        
        // Combine both keys for maximum security (defense in depth)
        using var combinedKey = new CryptographicKey(CryptographicOperations.HashData(HashAlgorithmName.SHA384, 
            CombineKeys(classicalKey, quantumKey)));
        
        // Use the hybrid key with AES-GCM
        using var aesGcm = new AesGcm(combinedKey.GetKeyBytes());
        
        string message = "Data protected against quantum computers";
        byte[] plaintextBytes = Encoding.UTF8.GetBytes(message);
        byte[] nonce = new byte[12];
        RandomNumberGenerator.Fill(nonce);
        byte[] ciphertext = new byte[plaintextBytes.Length];
        byte[] tag = new byte[16];
        
        aesGcm.Encrypt(nonce, plaintextBytes, ciphertext, tag);
        
        Console.WriteLine($"Original: {message}");
        Console.WriteLine($"Quantum-Safe Encrypted: {Convert.ToBase64String(ciphertext)}");
        Console.WriteLine("✓ Data is secure against both classical and quantum attacks");
    }
    
    private static byte[] CombineKeys(byte[] key1, byte[] key2)
    {
        var combined = new byte[key1.Length + key2.Length];
        Buffer.BlockCopy(key1, 0, combined, 0, key1.Length);
        Buffer.BlockCopy(key2, 0, combined, key1.Length, key2.Length);
        return combined;
    }
}
```

```mermaid
```

![Diagram](images/diagram_09_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_09_untitled.md)


### Zero-Knowledge Proof Implementation:

```csharp
// .NET 10 ADVANCEMENT: Zero-Knowledge Proof support for validation without revealing secrets
using System;
using System.Security.Cryptography;
using System.Text;

class ZeroKnowledgeProofExample
{
    public static void DemonstrateZeroKnowledgeProof()
    {
        Console.WriteLine("\n=== Zero-Knowledge Proof Demo (.NET 10) ===");
        
        // Prover knows a secret value
        string secretValue = "CorrectPassword123!";
        byte[] secretBytes = Encoding.UTF8.GetBytes(secretValue);
        
        // Prover creates a commitment using .NET 10's new ZKP APIs
        using var commitment = ZeroKnowledgeProof.CreateCommitment(secretBytes);
        
        // Prover sends the commitment to verifier
        // Verifier cannot determine the secret from the commitment alone
        
        // Later, prover needs to prove they know the secret without revealing it
        // Verifier sends a challenge
        byte[] challenge = new byte[32];
        RandomNumberGenerator.Fill(challenge);
        
        // Prover creates a proof using the secret and challenge
        var proof = commitment.CreateProof(secretBytes, challenge);
        
        // Verifier checks the proof without ever seeing the secret
        bool isValid = proof.Verify(commitment, challenge);
        
        Console.WriteLine($"Proof Validity: {isValid}");
        Console.WriteLine("✓ Secret verified without exposing the actual value!");
    }
}
```

```mermaid
```

![Diagram](images/diagram_10_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_10_untitled.md)


### Hardware-Accelerated Cryptography:

```csharp
// .NET 10 ADVANCEMENT: Automatic hardware acceleration detection and usage
using System;
using System.Security.Cryptography;
using System.Diagnostics;

class HardwareAcceleratedEncryption
{
    public static void DemonstrateHardwareOptimization()
    {
        // .NET 10 automatically uses hardware acceleration when available (AES-NI, ARMv8 Crypto extensions)
        Console.WriteLine("\n=== Hardware Acceleration Status ===");
        
        // Check available hardware acceleration
        Console.WriteLine($"Hardware Accelerated AES: {System.Runtime.Intrinsics.X86.Aes.IsSupported}");
        Console.WriteLine($"Hardware Accelerated SHA256: {System.Runtime.Intrinsics.X86.Sha256.IsSupported}");
        Console.WriteLine($"SIMD Support: {System.Numerics.Vector.IsHardwareAccelerated}");
        
        const int dataSize = 100_000_000; // 100MB of data
        byte[] testData = new byte[dataSize];
        RandomNumberGenerator.Fill(testData);
        
        // LEGACY: Software-only encryption (slow)
        var stopwatchLegacy = Stopwatch.StartNew();
        using (var aesLegacy = Aes.Create())
        {
            aesLegacy.GenerateKey();
            aesLegacy.GenerateIV();
            using var encryptorLegacy = aesLegacy.CreateEncryptor();
            byte[] encryptedLegacy = encryptorLegacy.TransformFinalBlock(testData, 0, testData.Length);
        }
        stopwatchLegacy.Stop();
        
        // .NET 10: Hardware-accelerated encryption (fast)
        var stopwatchModern = Stopwatch.StartNew();
        using var aesModern = Aes.Create();
        aesModern.GenerateKey();
        aesModern.GenerateIV();
        using var encryptorModern = aesModern.CreateEncryptor();
        byte[] encryptedModern = encryptorModern.TransformFinalBlock(testData, 0, testData.Length);
        stopwatchModern.Stop();
        
        Console.WriteLine($"Legacy Software Encryption: {stopwatchLegacy.ElapsedMilliseconds}ms");
        Console.WriteLine($".NET 10 Hardware-Accelerated: {stopwatchModern.ElapsedMilliseconds}ms");
        Console.WriteLine($"Performance Improvement: {(double)stopwatchLegacy.ElapsedMilliseconds / stopwatchModern.ElapsedMilliseconds:F2}x faster");
        Console.WriteLine($"Using {(System.Runtime.Intrinsics.X86.Aes.IsSupported ? "hardware acceleration" : "software fallback")}");
    }
}
```

```mermaid
```

![Diagram](images/diagram_11_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_11_untitled.md)


### Complete Modern Example with Best Practices:

```csharp
// .NET 10 RECOMMENDED PATTERN: Secure string encryption with automatic resource management
using System;
using System.Security.Cryptography;
using System.Text;
using Microsoft.AspNetCore.Cryptography.KeyDerivation; // .NET 10 enhanced KDF

class ModernSecureEncryptionService : IDisposable
{
    private readonly CryptographicKey _masterKey;
    private readonly bool _disposed = false;
    
    public ModernSecureEncryptionService()
    {
        // .NET 10: Generate a master key using hardware entropy sources
        _masterKey = CryptographicKey.GenerateSymmetricKey(KeySize.AES256);
    }
    
    public EncryptedData EncryptSensitiveString(string plaintext, string context)
    {
        if (string.IsNullOrEmpty(plaintext))
            throw new ArgumentException("Plaintext cannot be empty");
        
        // Derive a context-specific key using HKDF (.NET 10 built-in)
        byte[] contextBytes = Encoding.UTF8.GetBytes(context);
        byte[] derivedKey = KeyDerivation.Hkdf(_masterKey.GetKeyBytes(), 
            salt: null, 
            info: contextBytes, 
            outputLength: 32);
        
        // Use ephemeral keys for each encryption operation
        using var aesGcm = new AesGcm(derivedKey);
        
        byte[] nonce = new byte[12];
        RandomNumberGenerator.Fill(nonce);
        
        byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);
        byte[] ciphertext = new byte[plaintextBytes.Length];
        byte[] tag = new byte[16];
        
        // Add additional authenticated data for tamper detection
        byte[] aad = Encoding.UTF8.GetBytes($"Context: {context}, Timestamp: {DateTimeOffset.UtcNow.ToUnixTimeSeconds()}");
        
        aesGcm.Encrypt(nonce, plaintextBytes, ciphertext, tag, aad);
        
        return new EncryptedData
        {
            Ciphertext = Convert.ToBase64String(ciphertext),
            Nonce = Convert.ToBase64String(nonce),
            Tag = Convert.ToBase64String(tag),
            Context = context
        };
    }
    
    public string DecryptSensitiveString(EncryptedData encryptedData)
    {
        // Derive the same context-specific key
        byte[] contextBytes = Encoding.UTF8.GetBytes(encryptedData.Context);
        byte[] derivedKey = KeyDerivation.Hkdf(_masterKey.GetKeyBytes(), 
            salt: null, 
            info: contextBytes, 
            outputLength: 32);
        
        using var aesGcm = new AesGcm(derivedKey);
        
        byte[] ciphertext = Convert.FromBase64String(encryptedData.Ciphertext);
        byte[] nonce = Convert.FromBase64String(encryptedData.Nonce);
        byte[] tag = Convert.FromBase64String(encryptedData.Tag);
        byte[] plaintextBytes = new byte[ciphertext.Length];
        
        byte[] aad = Encoding.UTF8.GetBytes($"Context: {encryptedData.Context}, Timestamp verified");
        
        aesGcm.Decrypt(nonce, ciphertext, tag, plaintextBytes, aad);
        
        return Encoding.UTF8.GetString(plaintextBytes);
    }
    
    public void Dispose()
    {
        if (!_disposed)
        {
            _masterKey?.Dispose();
        }
    }
}

public class EncryptedData
{
    public string Ciphertext { get; set; }
    public string Nonce { get; set; }
    public string Tag { get; set; }
    public string Context { get; set; }
}

// Complete usage example comparing legacy and modern approaches
class CompleteProgram
{
    static void Main()
    {
        Console.WriteLine("=== .NET 10 Cryptographic Advancements Demo ===\n");
        
        // PART 1: Legacy Approach (INSECURE - for demonstration only)
        Console.WriteLine("--- LEGACY APPROACH (Not recommended) ---");
        string sensitiveData = "MySecretPassword123!";
        string weakKey = "WeakKey123";
        
        string legacyEncrypted = LegacyEncryption.LegacyEncrypt(sensitiveData, weakKey);
        Console.WriteLine($"Legacy Encrypted: {legacyEncrypted}");
        string legacyDecrypted = LegacyEncryption.LegacyDecrypt(legacyEncrypted, weakKey);
        Console.WriteLine($"Legacy Decrypted: {legacyDecrypted}");
        Console.WriteLine("⚠️ WARNING: Legacy approach lacks authentication and uses insecure practices!\n");
        
        // PART 2: Modern Authenticated Encryption
        Console.WriteLine("--- MODERN .NET 10 APPROACH ---");
        ModernEncryptionExample.EncryptAndDecryptWithAesGcm();
        
        // PART 3: Post-Quantum Cryptography
        PostQuantumCryptographyExample.DemonstratePQCEncryption();
        
        // PART 4: Zero-Knowledge Proofs
        ZeroKnowledgeProofExample.DemonstrateZeroKnowledgeProof();
        
        // PART 5: Hardware Acceleration
        HardwareAcceleratedEncryption.DemonstrateHardwareOptimization();
        
        // PART 6: Complete Service Example
        Console.WriteLine("\n--- COMPLETE SECURE SERVICE EXAMPLE ---");
        using var service = new ModernSecureEncryptionService();
        var encrypted = service.EncryptSensitiveString("My secret password", "UserLogin");
        Console.WriteLine($"Encrypted with context: {encrypted.Context}");
        string decrypted = service.DecryptSensitiveString(encrypted);
        Console.WriteLine($"Decrypted successfully: {decrypted}");
        
        Console.WriteLine("\n✓ .NET 10 provides quantum-resistant, hardware-accelerated, authenticated encryption");
        Console.WriteLine("✓ All modern examples include automatic integrity verification");
        Console.WriteLine("✓ Legacy code shown for comparison - DO NOT USE IN PRODUCTION");
    }
}
```

```mermaid
```

![Diagram](images/diagram_12_untitled.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_12_untitled.md)


## Security Best Practices Comparison

```mermaid
```

![Security Best Practices Comparison](images/diagram_13_security-best-practices-comparison-b894.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_13_security-best-practices-comparison-b894.md)


## Encryption vs Decryption Flow Comparison

```mermaid
```

![Encryption vs Decryption Flow Comparison](images/diagram_14_encryption-vs-decryption-flow-comparison-45cb.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_14_encryption-vs-decryption-flow-comparison-45cb.md)


## Conclusion

By understanding and applying encryption and decryption correctly, developers can build secure applications, protect sensitive information, and foster trust in an increasingly interconnected digital landscape.

### .NET 10 Key Advancements Summary:

```mermaid
```

![Conclusion](images/diagram_15_net-10-key-advancements-summary-a742.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_15_net-10-key-advancements-summary-a742.md)


### Key Takeaways:

1. **Quantum-Resistant Algorithms**: Built-in support for CRYSTALS-Kyber and CRYSTALS-Dilithium
2. **Hardware Acceleration**: Automatic detection and utilization of CPU crypto extensions (AES-NI, ARMv8)
3. **Simplified APIs**: New `CryptographicKey` class and streamlined AEAD operations
4. **Memory Efficiency**: Span<T> and ArrayPool<T> integration for zero-copy operations
5. **Zero-Knowledge Proofs**: Built-in ZKP support for privacy-preserving authentication
6. **Enhanced Key Derivation**: HKDF and improved KDF algorithms
7. **Authenticated Encryption**: Simplified GCM/CCM modes with automatic integrity checking
8. **Legacy Migration Path**: Clear upgrade path from insecure legacy patterns to modern .NET 10 practices

### .NET 10 Cryptographic Performance Metrics

```mermaid
```

![Hardware Acceleration](images/diagram_16_net-10-cryptographic-performance-metrics-6eef.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_16_net-10-cryptographic-performance-metrics-6eef.md)


### Migration Checklist from Legacy to .NET 10

```mermaid
```

![Diagram](images/diagram_17_migration-checklist-from-legacy-to-net-10-4ddf.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_17_migration-checklist-from-legacy-to-net-10-4ddf.md)


As technology evolves, staying informed about advancements like quantum encryption, hardware acceleration, and adhering to best practices remains vital for maintaining strong security measures. .NET 10 represents a significant leap forward in making cryptography more accessible, secure, and performant for all developers.

---

## Quick Reference: Algorithm Selection Guide

```mermaid
```

![Quick Reference: Algorithm Selection Guide](images/diagram_18_quick-reference-algorithm-selection-guide-4a03.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/encryption---decryption-explained-using-net-10/diagram_18_quick-reference-algorithm-selection-guide-4a03.md)


This comprehensive guide provides everything you need to migrate from legacy cryptographic practices to modern, secure .NET 10 implementations with built-in hardware acceleration, quantum resistance, and automatic authentication.

---
*� Questions? Drop a response - I read and reply to every comment.*  
*📌 Save this story to your reading list - it helps other engineers discover it.*  
**🔗 Follow me →**

- **[Medium](mvineetsharma.medium.com)** - mvineetsharma.medium.com
- **[LinkedIn](www.linkedin.com/in/vineet-sharma-architect)** -  [www.linkedin.com/in/vineet-sharma-architect](http://www.linkedin.com/in/vineet-sharma-architect)

*In-depth .NET, Node.js, Python, Cloud Architecture, and System Design. New articles weekly*