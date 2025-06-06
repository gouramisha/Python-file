

# Public access
print("Name:", account.name)            # ✅ works

# Protected access
print("Account Type:", account._account_type)  # ⚠️ works, but not recommended

# Private access
# print(account.__balance)             # ❌ ERROR: can't access directly

# Correct way to access private
print("Balance:", account.get_balance())       # ✅ YES!

# Even private can be accessed (not recommended)
print("Accessing hidden:", account._BankAccount__balance)  # ⚠️ works but unsafe
