# This is the repo I am working in ,it's in my GitHub:

This is the repo I am working in ,it's in my GitHub: https://github.com/stoner4kt/Conextsol-website-v2/tree/main .So my worker is returning this error in its logs :{
  "level": "error",
  "message": "POST https://contact-form-worker.reeqieric41.workers.dev/",
  "$workers": {
    "event": {
      "request": {
        "cf": {
          "isEUCountry": false,
          "tlsClientAuth": {
            "certRFC9440TooLarge": false,
            "certChainRFC9440TooLarge": false,
            "certPresented": "0",
            "certVerified": "NONE",
            "certRevoked": "0",
            "certIssuerDN": "",
            "certSubjectDN": "",
            "certIssuerDNRFC2253": "",
            "certSubjectDNRFC2253": "",
            "certIssuerDNLegacy": "",
            "certSubjectDNLegacy": "",
            "certSerial": "",
            "certIssuerSerial": "",
            "certSKI": "",
            "certIssuerSKI": "",
            "certFingerprintSHA1": "",
            "certFingerprintSHA256": "",
            "certNotBefore": "",
            "certNotAfter": "",
            "certRFC9440": "",
            "certChainRFC9440": ""
          },
          "httpProtocol": "HTTP/3",
          "clientAcceptEncoding": "gzip, deflate, br",
          "requestPriority": "",
          "colo": "JNB",
          "asOrganization": "SADV (Pty) Ltd",
          "country": "ZA",
          "city": "Cape Town",
          "continent": "AF",
          "region": "Western Cape",
          "regionCode": "WC",
          "timezone": "Africa/Johannesburg",
          "longitude": "18.42322",
          "latitude": "-33.92584",
          "postalCode": "7945",
          "tlsVersion": "TLSv1.3",
          "tlsCipher": "AEAD-AES128-GCM-SHA256",
          "tlsClientRandom": "uNyiGbM/qy77MpMq86VcP1bouxUFhqPLhzYl9J4W2Gc=",
          "tlsClientCiphersSha1": "3HTt3+R/6BL3zeALJDSq0pR1yOQ=",
          "tlsClientExtensionsSha1": "ZhpZkGj/PgSEsYGfPAVR/iHbjek=",
          "tlsClientExtensionsSha1Le": "S1oMuAe8/L6Q9U12gH7fLabf78c=",
          "tlsClientHelloLength": "321",
          "verifiedBotCategory": "",
          "edgeRequestKeepAliveStatus": 1,
          "clientTcpRtt": 0,
          "clientQuicRtt": 38,
          "asn": 37049,
          "edgeL4": {
            "deliveryRate": 59559
          }
        },
        "url": "https://contact-form-worker.reeqieric41.workers.dev/",
        "method": "POST",
        "headers": {
          "accept": "*/*",
          "accept-encoding": "gzip, br",
          "accept-language": "en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
          "cf-connecting-ip": "41.242.160.65",
          "cf-ipcountry": "ZA",
          "cf-ray": "a22de8f19ee53ed5",
          "cf-visitor": "{\"scheme\":\"https\"}",
          "connection": "Keep-Alive",
          "content-length": "184",
          "content-type": "application/json",
          "host": "contact-form-worker.reeqieric41.workers.dev",
          "origin": "https://conextsol.co.za",
          "priority": "u=1, i",
          "referer": "https://conextsol.co.za/",
          "sec-ch-ua": "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
          "sec-ch-ua-mobile": "?1",
          "sec-ch-ua-platform": "\"Android\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "cross-site",
          "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
          "x-forwarded-proto": "https",
          "x-real-ip": "41.242.160.65"
        },
        "path": "/"
      },
      "rayId": "a22de8f19ee53ed5",
      "response": {
        "status": 500
      }
    },
    "truncated": false,
    "scriptName": "contact-form-worker",
    "outcome": "ok",
    "eventType": "fetch",
    "executionModel": "stateless",
    "scriptVersion": {
      "id": "8753fc69-09d0-4b20-ae42-4ddbd4070471"
    },
    "requestId": "a22de8f19ee53ed5",
    "cpuTimeMs": 0,
    "wallTimeMs": 390
  },
  "$metadata": {
    "id": "01KYQFDMR5QR1T531437ADWJB9",
    "requestId": "a22de8f19ee53ed5",
    "rayId": "a22de8f19ee53ed5",
    "trigger": "POST /",
    "service": "contact-form-worker",
    "level": "error",
    "error": "POST https://contact-form-worker.reeqieric41.workers.dev/",
    "message": "POST https://contact-form-worker.reeqieric41.workers.dev/",
    "account": "02f41cc78664889233551c46dce02d52",
    "type": "cf-worker-event",
    "fingerprint": "cd8e891b12fbd05ad7258a749ca3f66b",
    "origin": "fetch",
    "messageTemplate": "POST https://contact-form-worker.reeqieric41.workers.dev/"
  }
}

Please analyze my repo and generate me a prompt that I can feed into Google ai studio to make the necessary changes, the worker is supposed to send the contact form submissions to my telegram bot so I get the notification with the form information, my telegram secrets are already set in my CloudFlare dashboard
