
USERNAME = "SecureSimon"
PASSWORD = "thisisalongandunbreakablepasswordyayyyyy"
Q1 = "Kingston"
Q2 = "1973"
Q3 = "Little Einsteins"

def validate_user(u, p) -> bool:
    return u == USERNAME and p == PASSWORD

def validate_security_questions(u, q1, q2, q3) -> bool:
    return  u == USERNAME and q1.strip().lower() == Q1.strip().lower() and q2.strip().lower() == Q2.strip().lower() and q3.strip().lower() == Q3.strip().lower() 