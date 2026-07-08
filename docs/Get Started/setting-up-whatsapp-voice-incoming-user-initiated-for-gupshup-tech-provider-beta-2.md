---
title: Guide to WhatsApp Voice & SIP Integration via Gupshup
excerpt: '##  Introduction'
deprecated: false
hidden: true
metadata:
  robots: index
---
WhatsApp Voice enables end-customers to initiate and receive calls via WhatsApp, creating a unified messaging and voice experience. Gupshup facilitates this capability through SIP integrations. This guide combines both product documentation and technical specifications for implementing incoming WhatsApp voice calls.

***

> 📘 Currently this offering is for select partners.

> 📘 If voice testing is not being done, please disable the voice icon. Leaving it enabled without proper setup can lead to the WABA being flagged or banned by Meta.

***

## Prerequisites

**From Tech Provider & Business:**

* Active WhatsApp phone number on Gupshup.
* SIP Voice setup with PSTN calling support.
* Audio Codec: `Opus/48000` (mandatory for compatibility).
* Call Routing: Ensure seamless forwarding with no failures.
* **Firewall Configuration**: No blocking of SIP or RTP traffic.
* **IP Whitelisting:**
  * Brazil: `54.207.112.105`
  * India: `35.154.159.246`
  * US: `3.225.218.184`
  > Ensure your firewall allows traffic to/from ephemeral ports (`1024–65535`).

***

> 📘 Support:
>
> ### For Beta issues, write directly to [aig.product@gupshup.io](mailto:aig.product@gupshup.io) for faster resolution

***

## <Anchor label="How to Enable WhatsApp Voice on WABA" target="_blank" href="https://partner-docs.gupshup.io/reference/post_partner-app-appid-voice#/">How to Enable WhatsApp Voice on WABA</Anchor>

**Step 1:** Partner initiates enablement via Partner API with SIP configuration.\
**Step 2:** Gupshup forwards the request to Meta.
**Step 3:** Meta responds:

* ✅ Success: `"Enable Voice - OK"`
* ❌ Failure: Error message with reason.

<Image align="center" src="https://files.readme.io/c75e88c0967b070b74f665c124f80462673a0b28bda46be0216dac2e883a7c46-3ce983a3258cc8ec2ced785acf2f9e11c544195a14a609d4adc30cbb6ccc1cf6-1.png" />

***

## SIP Configuration Options

### Basic SIP Call (No Registration)

* Scenario:
  * This configuration is used for direct SIP calling without registration. The SIP endpoint sends INVITE messages directly to the destination without establishing a prior registration.
* Use cases:
  * Direct SIP trunking between providers
  * Anonymous SIP calls
  * IP-to-IP direct calling
  * Some wholesale VoIP scenarios
* Example:

```json
{
  "host": "ip/domain",
  "port": "50X1"
}
```

* No REGISTER messages are sent
* INVITE messages go directly to the destination
* Often used with IP-based authentication instead of user credentials
* May require specific firewall/NAT traversal handling

No REGISTER messages sent. INVITE goes directly. Used with IP-based authentication.

***

## SIP Call With Authentication

* Scenario:
  * Registration is disabled, but authentication is still required.
    * This hybrid configuration is used when registration isn't needed but authentication is still required for outgoing calls. The SIP endpoint authenticates each INVITE rather than maintaining a registration.
* Use Cases:
  * SIP peering arrangements
  * Some SIP trunking scenarios
  * Cases where registration is undesirable but security is needed
  * Load balancer or proxy scenarios
* Example SIP Data

```json
{
  "host": "ip/domain",
  "port": "50X1",
  "secret_key": "XXXXXXXX18fc94ac1488b86c0XXXXX"
}
```

* Registration typically follows the SIP REGISTER message flow
* The client will periodically re-register based on the expiration time
* Authentication uses SIP digest authentication (usually MD5)

***

## Register True Without Authentication

* Scenario
  * This configuration is used when the SIP endpoint needs to register with the SIP server/proxy but does not require authentication.
* Use Cases
  * Internal SIP devices in trusted networks
  * Testing and development environments
  * Some legacy systems
  * Cases where IP-based authentication is used instead
* Example SIP Data:

```json
{
  "is_register": true,
  "username": "911XXXX258312",
  "host": "ip/domain",
  "port": "50X1",
  "secret_key": "XXXXXXXX18fc94ac1488b86c0XXXXX"
}
```

* Registration occurs without an authentication challenge
* The server typically identifies the client by IP address or MAC address
* Considered less secure - should only be used in controlled environments
* May still include From/To headers in REGISTER messages
* The server may apply other security measures (IP whitelisting, etc.)

***

## Note on Register

* Our platform acts as the User Agent Client (UAC) during registration. We register with your SIP server (Asterisk/FreeSWITCH/etc) and senda  call to you.
* This is the opposite of traditional phone-to-server registration

```
+---------------------+       +---------------------+
|   Our Platform      |       |  Your SIP Server    |
|   (UAC)             |       |  (UAS/Registrar)    |
|  Registers with     | SIP   |  Accepts            |
|  your server        |<----->|  registrations      |
+----------+----------+       +----------+----------+
           |                             |
           | RTP (Symmetric)             |
           +-----------------------------+
```

***

## TCP Transport Protocol Required

* Scenario
  * This configuration forces TCP as the transport protocol instead of the default UDP. TCP is used when message reliability or larger message sizes are required.
* Use Cases
  * Large SIP messages (many headers or SDP)
  * Networks with UDP reliability issues
  * Certain security requirements
  * NAT traversal scenarios where TCP works better
* Example SIP Data:

```json
{
  "is_register": true,
  "username": "911XXXX258312",
  "host": "ip/domain",
  "port": "50X1",
  "secret_key": "XXXXXXXX18fc94ac1488b86c0XXXXX",
  "force_tcp": true
}
```

* Uses SIP over TCP (RFC 3261)
* TCP provides reliable delivery, but with higher overhead
* The default SIP port remains 5060 (5061 for TLS)
* May require different keepalive mechanisms than UDP
* Often used as a fallback when UDP fails‌

***

## SIP Configuration Metadata Format

```json
[
  {
    "is_register": true,
    "user": "911XXXX258312",
    "username": "911XXXX258312",
    "host": "ip-XX-232-3-XX.ap-XXX-1.compute.internal",
    "port": "50X1",
    "secret_key": "XXXXXXXX18fc94ac1488b86c0XXXXX",
    "force_tcp": false
  }
]
```

| Parameter    | Description                                    | Type   | Required | Default       |
| ------------ | ---------------------------------------------- | ------ | -------- | ------------- |
| is\_register | Whether the SIP client needs to register       | Bool   | Yes      | false         |
| user         | Virtual SIP endpoint (user portion of SIP URI) | String | No       | Dialed Number |
| username     | SIP user or extension                          | String | No       | Dialer Number |
| host         | SIP server IP/domain                           | String | Yes      |               |
| port         | SIP URI forward port                           | String | Yes      |               |
| secret\_key  | Password used for registration                 | String | No       | Blank String  |
| force\_tcp   | Whether to use TCP instead of UDP              | Bool   | No       | false         |

> 📘 username\@host:port : “sip:[912250142880@ip-10-x.x.x.ap-south-1.compute.internal](mailto:912250142880@ip-10-x.x.x.ap-south-1.compute.internal):5071”. ( sip URI )

***

## SIP Registration Flow Diagram

```
+-------------+          +-------------+
 | Gupshup SIP |          | SIP Server  |
 |  Client     |          | (Registrar) |
 +-------------+          +-------------+
       |                        |
       |---- REGISTER --------->|
       |<-- 401 Unauthorized ---|
       |-- REGISTER (auth) ---->|
       |<------ 200 OK ---------|
```

***

## SIP INVITE Flow (For Incoming Calls)

```
+--------+         +----------+         +--------+
 | Caller |         |  SIP     |         | Callee |
 | Agent  |         |  Server  |         | Agent  |
 +--------+         +----------+         +--------+
     |                  |                     |
     |---- INVITE ----->|                     |
     |<-- 100 Trying ---|                     |
     |                  |---- INVITE -------> |
     |                  |<-- 180 Ringing ---- |
     |<-- 180 Ringing --|                     |
```

SIP works over Symmetric Response Routing — <Anchor label="RFC3581" target="_blank" href="https://datatracker.ietf.org/doc/html/rfc3581">RFC3581</Anchor>

***

## Sample SIP INVITE Payload

```text
INVITE sip:91XXXXXXXX@ip-XXX-XXX-XXX-XXX.ap-south-1.compute.internal:5071 SIP/2.0
Via: SIP/2.0/UDP XXX.XXX.XXX.XXX:XXXXX;rport;branch=z9hG4bKXXXXXXXXXXX
Max-Forwards: 70
From: "+91XXXXXXXXXX" <sip:+91XXXXXXXXXX@ip-XXX-XXX-XXX-XXX.ap-south-1.compute.internal:5071>;tag=XXXXXX
To: <sip:91XXXXXXXX@ip-XXX-XXX-XXX-XXX.ap-south-1.compute.internal:5071>
Call-ID: wacid.XXXXXXXXXXXXXXXXXX
CSeq: XXXXXXXXX INVITE
Contact: <sip:+91XXXXXXXXXX@XXX.XXX.XXX.XXX:XXXXX;transport=udp>
User-Agent: Gupshup WebRTC Gateway
Allow: INVITE, ACK, BYE, CANCEL, OPTIONS, REFER, MESSAGE, INFO, NOTIFY
Supported: replaces
Content-Type: application/sdp
Content-Disposition: session
Content-Length: 451
X-WV-CALLID: wacid.XXXXXXXXXXXXXXX
X-WV-FROM: +91XXXXXXXXXX
X-WV-TO: +91XXXXXXXX
v=0
o=- XXXXXXX IN IP4 XXX.XXX.XXX.XXX
s=-
t=0 0
a=ice-lite
m=audio XXXXX RTP/AVP 111 126
c=IN IP4 XXX.XXX.XXX.XXX
a=rtpmap:111 opus/48000/2
a=fmtp:111 maxaveragebitrate=20000;maxplaybackrate=16000;minptime=20;sprop-maxcapturerate=16000;useinbandfec=1
a=rtpmap:126 telephone-event/8000
a=mid:audio
a=msid:XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX WhatsAppTrack1
a=rtcp-fb:111 transport-cc
a=maxptime:20
a=ptime:20

```

***

## Media & RTP Requirements

* OPUS/48000 for codec, since the RTP clock rate is set at 48000 in SDP as per the <Anchor label="RFC" target="_blank" href="https://datatracker.ietf.org/doc/html/rfc7587#autoid-17">RFC</Anchor>.
  * Partners using Twilio can face some issues with their default support being for g711.
  * fmtp can suggest maxaveragebitrate=20000;maxplaybackrate=16000;minptime=20;sprop maxcapturerate=16000;useinbandfec=1 , but with opus 48k
* DTMF coming through the RTP data stream.
  * <Anchor label="rfc4733" target="_blank" href="https://datatracker.ietf.org/doc/html/rfc4733">rfc4733</Anchor> ; a=rtpmap:126 telephone-event/8000
* Symmetrical RTP Requirement
  * <Anchor label="rfc4961" target="_blank" href="https://datatracker.ietf.org/doc/html/rfc4961">rfc4961</Anchor>
  * We send the Symmetric RTP Requirement
  * Infra should allow symmetric RTP
  * Ensures media flows through the same path as the signalling
  * It will be expected that RTP packets to be sent from the same IP/port combination that was negotiated in SDP

***

## Billing Events API (Sample Payload)

```json
{
  "call": {
    "id": "wacid.XXXXXXXXXXXXX",
    "to": "16315XXX601",
    "from": "16315XX3602",
    "event": "terminate",
    "direction": "incoming",
    "timestamp": 1671644824,
    "status": "Completed",
    "start_time": 1671644824,
    "end_time": 1671644944,
    "duration": 120
  },
  "phone": "780XXX7021",
  "conversationType": "CALL",
  "isGsBilling": true,
  "appId": "269a4153-XXX-4590-XXXX-6e2e937836e4",
  "billable": true
}
```

***

## Voice Analytics

Available on Partner Analytics Dashboard. Only incoming call events and duration are shown.

<Image align="center" src="https://files.readme.io/1ea4d4e4b4c9441e498cf74940217dc65e8d2d590831a5e4bf090791c7eba1f4-7f4eaaa42d4141eb383d8669bac9485f597c51ad4131c86ef8158166db463449-voice2.png" />

> 📘 Only Incoming voice events count of minutes will be shown

> 📘 The caller can be from any region, but latency may vary based on the caller’s location.

> 📘 Inbound Voice calls are free of charge by Meta

***

OUTGOING CALL (Business initiated)\
(Tier-based pricing for higher than 50,000 call minutes per month will also be available from Meta. Check **<Anchor label="here" target="_blank" href="https://developers.facebook.com/docs/whatsapp/cloud-api/calling/pricing#volume-based-pricing--vbp--rate-card">here</Anchor>**)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Voice Call Rates (Effective August 01)

| Market (per rate card)           | Currency | NEW Rate - Aug 01 (cost per minute) |
| -------------------------------- | -------- | ----------------------------------- |
| Argentina                        | $US      | 0.0101                              |
| Brazil                           | $US      | 0.0108                              |
| Chile                            | $US      | 0.0121                              |
| Colombia                         | $US      | 0.0111                              |
| France                           | $US      | 0.0099                              |
| Germany                          | $US      | 0.0103                              |
| India                            | $US      | 0.0053                              |
| Indonesia                        | $US      | 0.0242                              |
| Israel                           | $US      | 0.0127                              |
| Italy                            | $US      | 0.0121                              |
| Malaysia                         | $US      | 0.0108                              |
| Mexico                           | $US      | 0.0094                              |
| Netherlands                      | $US      | 0.0063                              |
| Pakistan                         | $US      | 0.0119                              |
| Peru                             | $US      | 0.0121                              |
| Russia                           | $US      | 0.0097                              |
| Saudi Arabia                     | $US      | 0.0127                              |
| South Africa                     | $US      | 0.0108                              |
| Spain                            | $US      | 0.0129                              |
| United Arab Emirates             | $US      | 0.0127                              |
| United Kingdom                   | $US      | 0.0099                              |
| Rest of Africa                   | $US      | 0.0103                              |
| Rest of Asia Pacific             | $US      | 0.0114                              |
| Rest of Central & Eastern Europe | $US      | 0.0095                              |
| Rest of Latin America            | $US      | 0.0116                              |
| Rest of Middle East              | $US      | 0.0127                              |
| Rest of Western Europe           | $US      | 0.0103                              |
| Other                            | $US      | 0.0132                              |

***