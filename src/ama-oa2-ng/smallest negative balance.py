from typing import List
def debtRecords(numCols: int, numRows: int, debts: List[List[str]]) -> List[str]:
    default = "Nobody has a negative balance"
    accounts = {}

     if not debts:
        return [default]
    
    for entry in debts:
        borrower = entry[0]
        lender = entry[1]
        amount = int(entry[2])
        accounts[borrower] = accounts.get(borrower, 0) - amount
        accounts[lender] = accounts.get(lender, 0) + amount
    negative_accounts = []

    for person in accounts:
        if accounts[person] < 0:
            negative_accounts.append((accounts[person], person))
    negative_accounts.sort()

    if len(negative_accounts) > 0:
        return [entry[1] for entry in negative_accounts]
    else:
        return [default]
