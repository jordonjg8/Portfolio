# Jordon Grissom
# Portfolio Project: Enterprise Transaction Ledger Engine

class TransactionLedger:
    def __init__(self, account_holder: str, initial_deposit: float):
        self.holder = account_holder
        self.__balance = initial_deposit  # Private variable to prevent unauthorized manipulation
        self.history = []
        self._log_transaction("INITIAL_DEPOSIT", initial_deposit, success=True)

    def _log_transaction(self, type: str, amount: float, success: bool, reason: str = "Approved"):
        """Logs internal system events securely."""
        self.history.append({
            "type": type,
            "amount": amount,
            "success": success,
            "status_reason": reason
        })

    def process_withdrawal(self, amount: float) -> bool:
        """Evaluates and processes debit requests against available liquidity."""
        if amount <= 0:
            self._log_transaction("WITHDRAWAL", amount, success=False, reason="Invalid Amount")
            return False
            
        if self.__balance - amount < 0:
            self._log_transaction("WITHDRAWAL", amount, success=False, reason="Insufficient Funds / Overdraft Blocked")
            return False

        self.__balance -= amount
        self._log_transaction("WITHDRAWAL", amount, success=True)
        return True

    def get_ledger_summary(self):
        """Generates a structural report of the current account state."""
        return {
            "Account Holder": self.holder,
            "Liquid Capital": f"${self.__balance:,.2f}",
            "Transaction Count": len(self.history),
            "Audit Trail": self.history
        }

# ==========================================
# SIMULATION ENGINE (Execution Pipeline)
# ==========================================
if __name__ == "__main__":
    # Initialize a secure account for Jordan with $1,000
    account = TransactionLedger(account_holder="Jordan Grissom", initial_deposit=1000.00)
    
    # Process complex real-world transactions
    account.process_withdrawal(45.50)   # Valid purchase
    account.process_withdrawal(1200.00) # Fraudulent / Overdraft attempt (Will be safely blocked)
    account.process_withdrawal(5.00)    # Valid purchase
    
    # Generate system audit summary
    summary = account.get_ledger_summary()
    
    print(f"\n--- SYSTEM AUDIT: {summary['Account Holder'].upper()} ---")
    print(f"Current Liquidity: {summary['Liquid Capital']}")
    print(f"Total Logged Events: {summary['Transaction Count']}\n")
    print("LOGGED AUDIT TRAIL:")
    for event in summary['Audit Trail']:
        status = "PASSED" if event['success'] else "FAILED"
        print(f"  [{status}] {event['type']}: ${event['amount']:.2f} | Reason: {event['status_reason']}")
