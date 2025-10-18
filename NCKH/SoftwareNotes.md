**JWT** : JSON Web Tokens
- Is used for Authorization : Make sure the user that is sending requests to the server is the same user that logged in via the authentication process
- The way Authorization is done is via session, which is sent to the server to verify before sending back a response
- With JWT, the server doesn't need to store the user's info. It encrypts infos with a specific sercret key, which makes it hard to tamper/hack
  - Because the info is stored in the JWT, not in the server
  - Most JWT has IAT : Issued at, and expired date. 
  - To note, remember to save the secret key somewhere in the server inaccessible to ANYONE
- Similar to password hashing
- Can be used to have the same login info between two different servers from the same website OR different WEBSITES using the same secret key
-  With a lot of microservices, you can use JWT to access the microservices across different architecture

A JSON Web Token (JWT) is a secure way to send information between a client and a server. It is mainly used in web applications and APIs to verify users and prevent unauthorized access. A JWT is JSON data secured with a cryptographic signature.
-
JWT's structure includes :
- Header : Contains metadata about the token, along with the signing algorithm and token type(always JWT)
- Payload : The actual information about the user, often accompanied with timestamps of when the request is issued or expired. The common claim types are:
  - iss (Issuer): Identifies who issued the token.
  - sub (Subject): Represents the user or entity the token is about.
  - aud (Audience): Specifies the intended recipient.
  - exp (Expiration): Defines when the token expires.
  - iat (Issued At): Timestamp when the token was created.
  - nbf (Not Before): Specifies when the token becomes valid.
- Signature : Verify the JWT sent to the server via the secret key, and the encryptid header+payload
