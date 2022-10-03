# githubactionstrackr

CI-CD of a Flutter project.

#### Github secrets for Auto release.


| Secrets | Purpose | Where to generate | 
| --- | --- | --- |
| APPSTORE_API_KEY_ID | Upload app to TestFlight | https://appstoreconnect.apple.com/access/api |
| APPSTORE_API_PRIVATE_KEY | Upload app to TestFlight | https://appstoreconnect.apple.com/access/api |
| APPSTORE_ISSUER_ID | Upload app to TestFlight | https://appstoreconnect.apple.com/access/api |
| MOBILEPROVISION_BASE64 | App signing | https://developer.apple.com/account/resources/profiles/list |
| MOBILEPROVISION_NAME | App signing | https://developer.apple.com/account/resources/profiles/list |
| P12_BASE64 | App signing | Export P12 from KeyChain on Mac device after installing certificate from -> https://developer.apple.com/account/resources/certificates/list |
| TEAM_ID | App signing | https://developer.apple.com/account/#!/membership/ |