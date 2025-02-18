# Miku's Autograph

## Flag
bronco{miku_miku_beaaaaaaaaaaaaaaaaaam!}

## Intended Solution:
This challenge revolves around a common JWT (JSON Web Token) vulnerability where the server incorrectly accepts none as a valid signing algorithm. The goal is to forge a JWT token that allows us to authenticate as miku_admin and retrieve the flag.

In a secure JWT implementation, the signature prevents modification of the header or payload.

The miku fan club page incorrectly allows JWTs with alg: "none", meaning no signature is required. By setting alg: "none", we can bypass authentication and become miku_admin without knowing the secret key.

First, we need a valid token to inspect how the server structures its JWTs. We can get the token through the magic login request: /get_token

When looking at the token, we can see its structure and see this token is signed using HS256, meaning it requires a signature.

Decoding the JWT, we can see its content. 

This tells us that subject controls the username, so we need to set sub: "miku_admin" to gain access.

We will manually create an unsigned JWT with alg: "none" and sub: "miku_admin".

HEADER: { "alg": "none", "typ": "JWT" }
PAYLOAD: { "sub": "miku_admin" }

Since alg is none, we do not need a signature.

Intercept the token, with Burp or something else, modify to use an unsigned JWT afforementioned, and you will get the flag!
