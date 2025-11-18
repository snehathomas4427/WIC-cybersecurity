#Password Strength Checker

"""
OBJECTIVE: Build a simple password checker that tests if passwords are secure
INSTRUCTIONS: Fill in the 5 functions below where it says "YOUR CODE HERE"
"""

# List of commonly hacked passwords
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "password123", "admin", "letmein", "welcome", "monkey"
]


def has_uppercase(password):
    """
    TODO: Check if password has at least one uppercase letter (A-Z)
    
    Return True if it does, False if it doesn't
    
    HINT: Loop through each character and check if char.isupper()
    """
    # YOUR CODE HERE
    pass


def has_digit(password):
    """
    TODO: Check if password has at least one number (0-9)
    
    Return True if it does, False if it doesn't
    
    HINT: Loop through each character and check if char.isdigit()
    """
    # YOUR CODE HERE
    pass


def has_special_character(password):
    """
    TODO: Check if password has at least one special character (!@#$%^&*)
    
    Return True if it does, False if it doesn't
    
    HINT: Check if any character is in the string "!@#$%^&*"
    """
    # YOUR CODE HERE
    pass

def is_common_password(password):
    """Check if the password is in the common passwords list"""
    pass


def has_repeated_characters(password):
    """Check if password has 3 or more of the same character in a row"""
    pass


# ========== ALREADY COMPLETE - NO NEED TO EDIT ==========

def check_password_security(password):
    """This function uses your code above to check password security"""
    print(f"\nAnalyzing password: {password}")
    print("=" * 50)
    
    issues = []
    score = 100  # Start with perfect score
    
    # Check length
    if len(password) >= 8:
        print("✓ Length is good (8+ characters)")
    else:
        print("✗ Too short (needs 8+ characters)")
        issues.append("too short")
        score -= 30
    
    # Check uppercase
    if has_uppercase(password):
        print("✓ Has uppercase letter")
    else:
        print("✗ Missing uppercase letter")
        issues.append("no uppercase")
        score -= 15
    
    # Check digit
    if has_digit(password):
        print("✓ Has number")
    else:
        print("✗ Missing number")
        issues.append("no number")
        score -= 15
    
    # Check special character
    if has_special_character(password):
        print("✓ Has special character")
    else:
        print("✗ Missing special character (!@#$%^&*)")
        issues.append("no special character")
        score -= 15
    
    # Check if it's a common password (SECURITY RISK!)
    if is_common_password(password):
        print("✗ 🚨 WARNING: This is a commonly hacked password!")
        issues.append("commonly hacked")
        score -= 40
    else:
        print("✓ Not in common passwords database")
    
    # Check for repeated characters (SECURITY RISK!)
    if has_repeated_characters(password):
        print("✗ ⚠️  Contains repeated characters (e.g., 'aaa', '111')")
        issues.append("repeated characters")
        score -= 20
    else:
        print("✓ No obvious repeated patterns")
    
    # Ensure score doesn't go negative
    score = max(0, score)
    
    # Final verdict
    print("=" * 50)
    print(f"SECURITY SCORE: {score}/100")
    
    if score >= 90:
        print("🎉 STRONG PASSWORD - Well done!")
    elif score >= 70:
        print("⚠️  MODERATE PASSWORD - Consider improvements")
    elif score >= 50:
        print("❌ WEAK PASSWORD - Easily cracked")
    else:
        print("🚨 VERY WEAK PASSWORD - Change immediately!")
    
    if issues:
        print(f"\nIssues found: {', '.join(issues)}")
    print("=" * 50)


# Test your code with these passwords
print("=" * 50)
print("PASSWORD SECURITY CHECKER")
print("=" * 50)
print("\nTesting various passwords...\n")

test_passwords = [
    "password",          # Common password
    "Password123",       # Missing special char
    "Pass123!",          # Too short
    "Helllo123!",        # Has repeated chars (lll)
    "MyP@ssw0rd2024",    # Strong password
]

for pwd in test_passwords:
    check_password_security(pwd)

print("\n" + "=" * 50)
print("Now test your own passwords above!")
print("=" * 50)
