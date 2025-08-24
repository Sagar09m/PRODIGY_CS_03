import re

def check_password_complexity(password):
    """Checks the complexity of a password based on several criteria."""
    
    # --- Criteria ---
    min_length = 8
    score = 0
    feedback = []

    # 1. Check Length
    if len(password) >= min_length:
        score += 1
        feedback.append("✔️ Password length is sufficient.")
    else:
        feedback.append(f"❌ Password must be at least {min_length} characters long.")

    # 2. Check for Uppercase Letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✔️ Contains uppercase letters.")
    else:
        feedback.append("❌ Must contain at least one uppercase letter (A-Z).")

    # 3. Check for Lowercase Letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✔️ Contains lowercase letters.")
    else:
        feedback.append("❌ Must contain at least one lowercase letter (a-z).")

    # 4. Check for Numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✔️ Contains numbers.")
    else:
        feedback.append("❌ Must contain at least one number (0-9).")
    
    # 5. Check for Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✔️ Contains special characters.")
    else:
        feedback.append("❌ Must contain at least one special character (!, @, #, etc.).")

    # --- Final Assessment ---
    print("\n--- Password Complexity Report ---")
    print(f"Password: '{password}'")
    
    for item in feedback:
        print(item)
    
    print("\n--- Overall Strength ---")
    if score == 5:
        print("🟢 Strong! Your password is very secure.")
    elif score >= 3:
        print("🟡 Medium! Your password is moderately secure.")
    else:
        print("🔴 Weak! Your password needs improvement.")

# --- Main execution part ---
if __name__ == "__main__":
    while True:
        user_password = input("\nEnter a password to check its complexity (or type 'exit' to quit): ")
        if user_password.lower() == 'exit':
            break
        check_password_complexity(user_password)
        print("-" * 40)
