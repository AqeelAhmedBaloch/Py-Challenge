import re

def check_joinur_password(password):
    # Basic checks
    length_score = min(len(password) // 2, 5)  # Up to 5 points for length
    upper_score = 1 if any(c.isupper() for c in password) else 0
    lower_score = 1 if any(c.islower() for c in password) else 0
    digit_score = 1 if any(c.isdigit() for c in password) else 0
    special_score = 1 if bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)) else 0
    
    total_score = length_score + upper_score + lower_score + digit_score + special_score
    
    # English style messages
    if len(password) < 6:
        return "Password Strength: Very Weak ❌"
    
    if total_score < 5:
        return "⚠️ Warning: Password is weak! Please make it stronger"
    elif total_score < 7:
        return "✅ Password is good, but could be better"
    else:
        return "🔒 Excellent! Password is very strong"

# Main program
print("🔑 Password Strength Checker 🔑")
print("=" * 30)

while True:
    password = input("\nEnter password to check (or 'Q' to quit): ")
    if password.lower() == 'q':
        print("Thank you for using! 👋")
        break
    
    result = check_joinur_password(password)
    print(result)
    
    if '❌' not in result:
        suggestion = "\nTips for stronger password:"
        if len(password) < 8:
            suggestion += "\n- Make the password longer"
        if not any(c.isupper() for c in password):
            suggestion += "\n- Add capital letters"
        if not any(c.isdigit() for c in password):
            suggestion += "\n- Include numbers"
        if not bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
            suggestion += "\n- Add special characters (@#$%)"
        if suggestion != "\nTips for stronger password:":
            print(suggestion)
