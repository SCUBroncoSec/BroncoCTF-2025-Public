# BroncoCTF-2025-Internal

This is the *public* repo for BroncoCTF 2025. Files for the public release of BroncoCTF run should be stored here.

## Directory Structure

```
BroncoCTF-2025-Public/
├── README.md
├── Challenges/
    └── README.md
    └── <Challenge Category>/
        └── <Challenge Name>/
            ├── Infra/
            ├── Files/
            ├── README.md
            └── Solution.md (or PDF)
```
The organization for this repo should be easy to understand. The only files in the root directory should be system files (such as .gitignore, etc.), and files that explain where everything is (this README). Everything else is in a subfolder who's name should succinctly describe it's purpose (Challenges/ holds challenges). It's also a smart idea for subfolders to have README that explains the folder's specific purpose, just so people have a good idea of what's going on.

The reason we do all of this is to make it easy for current board members to contribute to BroncoCTF, and make it easy for future board members to understand pervious BroncoCTF infrastructure.