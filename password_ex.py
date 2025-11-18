#Password Strength Checker

"""
OBJECTIVE: Build a simple password checker that tests if passwords are secure
INSTRUCTIONS: Fill in the THREE functions below where it says "YOUR CODE HERE"
"""

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


# ========== ALREADY COMPLETE - NO NEED TO EDIT ==========

def check_password_strength(password):
    """This function uses your code above to check password strength"""
    print(f"\nChecking password: {password}")
    print("-" * 40)
    
    # Check length
    if len(password) >= 8:
        print("✓ Length is good (8+ characters)")
        length_ok = True
    else:
        print("✗ Too short (needs 8+ characters)")
        length_ok = False
    
    # Check uppercase
    if has_uppercase(password):
        print("✓ Has uppercase letter")
        upper_ok = True
    else:
        print("✗ Needs uppercase letter")
        upper_ok = False
    
    # Check digit
    if has_digit(password):
        print("✓ Has number")
        digit_ok = True
    else:
        print("✗ Needs number")
        digit_ok = False
    
    # Check special character
    if has_special_character(password):
        print("✓ Has special character")
        special_ok = True
    else:
        print("✗ Needs special character (!@#$%^&*)")
        special_ok = False
    
    # Final result
    if length_ok and upper_ok and digit_ok and special_ok:
        print("\n🎉 STRONG PASSWORD!")
    else:
        print("\n❌ WEAK PASSWORD - Fix the issues above")
    print("-" * 40)


# Test your code with these passwords
print("=" * 40)
print("PASSWORD STRENGTH CHECKER")
print("=" * 40)

test_passwords = [
    "password",          # Weak - no uppercase, digit, or special
    "Password123",       # Weak - no special character
    "Pass123!",          # Weak - too short
    "Password123!",      # Strong - has everything
]

for pwd in test_passwords:
    check_password_strength(pwd)