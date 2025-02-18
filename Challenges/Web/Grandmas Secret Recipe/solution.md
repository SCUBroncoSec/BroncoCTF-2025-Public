# Grandma’s Secret Recipe

## Flag


## Intended Solution:
When visiting /, users receive a role=user cookie.
The system validates the role using an MD5 checksum stored in a separate checksum cookie.
Understand the Vulnerability

The app verifies access using:
```
checksum = hashlib.md5(role.encode()).hexdigest()
```

If a user modifies their role cookie, the corresponding checksum must also match MD5(new_role).

Change the role from 'kithen helper' to 'grandma'.
```
MD5("grandma") = a5d19cdd5fd1a8f664c0ee2b5e293167
```

Set the cookies manually using browser dev tools or a proxy 
```
role="grandma"
checksum=a5d19cdd5fd1a8f664c0ee2b5e293167
```
After modifying cookies, visit /grandma.
The flag will be revealed.
