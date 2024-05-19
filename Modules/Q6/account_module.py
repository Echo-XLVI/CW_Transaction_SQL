from dbmanager_module import DataBaseManager as dbm
class Account:
    def __init__(self, acc_id:str, balance:int) -> None:
        self.acc_id=acc_id
        self.balance=balance

    def check_balance(self, amount:int) ->bool:
        res=dbm.select('account', {'acc_id':self.acc_id})
        if res[2]>amount:
            return True
        return False

    def transfer(self, amount:int, to_acc_id:str) -> None:
        if self.check_balance(amount):
            dbm.update('account',set={'balance':f"balance+{amount}"},where={'acc_id':to_acc_id})
            dbm.update('account',set={'balance':f"balance-{amount}"},where={'acc_id':self.acc_id})
        else:
            return "balance is not enough"

ac1=Account(3,200000)    
ac1.check_balance(600)
ac1.transfer(200,2)