# Challenges

This is the directory where individual challenges are stored. Challenges are placed in subfolders that denote their category.

## Directory Structure

```
Challenges/
└── README.md
└── <Challenge Category>/
    └── <Challenge Name>/
        ├── Infra/
        ├── Files/
        ├── README.md
        └── Solution.md
```

Each challenge has its own folder inside the folder corresponding to its category (The "challenge folder"). The challenge folder doesn't need to share the same name as the actual challenge on the CTF website, but instead should be breif and descriptive of what the challenge is.

Each challenge folder should contain the following:

- Infra/
    - Only required if the challenge needs hosted infra
    - This folder contains all of the hosted infrastructure (server side code/configs) required for the challenge
    - Ideally, this folder should be set up so that it can be easily ran via Google Cloud Run
- Files/
    - This folder contains anything that is distributed to participants through a download.
- README.md
    - Contains basic info about the challenge such as:
        - Name (as shown on CTF website)
        - Description (as shown on CTF website)
- Solution
    - A solution guide for the challenge
    - Should be in markdown