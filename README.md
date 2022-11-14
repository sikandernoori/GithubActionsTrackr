# githubactionstrackr

CI-CD of a Flutter project.


#### Github secrets for Auto release.


| Secrets | Purpose | Where to generate | 
| --- | ---- | --- |
| APPSTORE_API_KEY_ID | Upload app to TestFlight | https://appstoreconnect.apple.com/access/api |
| APPSTORE_API_PRIVATE_KEY | Upload app to TestFlight | https://appstoreconnect.apple.com/access/api |
| APPSTORE_ISSUER_ID | Upload app to TestFlight | https://appstoreconnect.apple.com/access/api |
| MOBILEPROVISION_BASE64 | App signing | https://developer.apple.com/account/resources/profiles/list |
| MOBILEPROVISION_NAME | App signing | https://developer.apple.com/account/resources/profiles/list |
| P12_BASE64 | App signing | Export P12 from KeyChain on Mac device after installing certificate from -> https://developer.apple.com/account/resources/certificates/list |
| TEAM_ID | App signing | https://developer.apple.com/account/#!/membership/ |

##### 1. Appstore API Key
This step help obtaining `APPSTORE_ISSUER_ID`, `APPSTORE_API_KEY_ID` and `APPSTORE_API_PRIVATE_KEY`  
To generate keys, you must have an Admin account in App Store Connect. You may generate multiple API keys with any roles you choose for purpose of this project create API key with App Manager level role.

To generate an API key to use with the App Store Connect API, log in to [App Store Connect](https://appstoreconnect.apple.com/).
```
  i. Select Users and Access, and then select the API Keys tab.

  ii. Click Generate API Key or the Add (+) button.

  iii. Enter a name for the key. The name is for your reference only and is not part of the key itself.

  iv. Under Access, select the role for the key. (For CI/CD App Manager level role is sufficient)

  v. Click Generate.
```
The new key's name, key ID, a download link, and other information appears on the page.

##### Download and Store the Private Key
Once you've generated your API key, you are given the opportunity to download the private half of the key. The private key is available for download a single time.

The download link appears only if the private key has not yet been downloaded. Apple does not keep a copy of the private key.
Store your private key in a safe place.

***Important***

***Keep your API keys secure and private. You should never share your keys, store keys in a code repository, or include keys in client-side code.***

***If the key becomes lost or compromised, remember to revoke it immediately. See Revoking API Keys for more information.***
   
![Appstore_IssuerID_API_KEY_ID](https://user-images.githubusercontent.com/16399272/193779375-9890b7f8-75c2-455a-bb60-c3bcc8089ca4.png)

##### 2. Mobileprovision
  Mobileprovision profile is required to sign the app binaries.
  
  To generate .mobileprovision profile, log in to [Apple developer portalt](https://developer.apple.com/account/).
```
  i. Certificates, Identifiers & Profiles, and then select the Profile tab.

  ii. Click Generate profile or the Add (+) button.

  iii. Under `Distribution` select `App Store` and click Continue.

  iv. Select an App ID and lcick Continue

  v. Select appropriate distribution certificate and click Continue.
  
  vi. Insert profile name (important, this name will be used as `MOBILEPROVISION_NAME`) and click generate profile.
  
  vii. Download profile and convert it to base64 string and use it as `MOBILEPROVISION_BASE64`
  
  ```
  
  TODO(skandar) Drag drop provisioning profile screenshot.
  
##### 3. p12 Certificate.
  Certificate required to sign the app binaries.
    
  To generate .p12 certificate, log in to [Apple developer portalt](https://developer.apple.com/account/).
    
```
  i. Certificates, Identifiers & Profiles, and then select the Certificates tab.
  
  ii. Click Generate Certificate or the Add (+) button. 
  
  iii. select iOS Distribution (App Store and Ad Hoc) under Software and click Continue.
  
  iv. Upload a Certificate Signing Request and click Continue. (how to generate signing request check section 4 (TODO skandar add link))
  
  v. Download iOS Distribution certificate and install them to Local Keychain by double clicking.
  
  vi. Open KeyChain and right Click on iOS Distribution certificate installed in above step and select Export `.p12` certificate.
  
  vii Convert .p12 certificate file into base64 and use it as `P12_BASE64`.
  
```
  
##### 4. Signing request certificate.
  Signing request certificate is required to generate development and distribution certificates in apple developer portal.
    
  To generate signing request certificate open keychain on your MacBook and click `Request a Certificate from a Certificate Authourity` under `Certificate Assistant` as shown in below screenshot.
    
    TODO(skandar) add screenshot here