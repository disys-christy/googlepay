class Google_pay:                                                                                   
    
    def __init__(self):
        print("transaction")
        self.name=input("enter name:")
        self.mobile=input("enter mobile number:")
        self.otp=input("enter otp:")
        self.bank=input("enter account number:")
        self.pin=input("set pin:")
        
    def open_gpay(self):
        print("transaction successsfull")

    def name_verification(self):
        if type(self.name) == str:
            if len(self.name) <= 20:                                                                                
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")

    def mobile_verification(self):
        if (len(self.mobile)==10):
            if type(self.mobile) == str:                                                            
                print("phone number verified")
            else:
                raise ValueError("invalid number")


    def otp_verf(self):
        if (type(self.otp)==int):
            print("otp verified")
       
    def bank_verification(self):
        self.Account=[]
        self.Account_number=3426789012
        self.Account.append(self.Account_number)                                                                    
        print(self.Account)
        print("Bank account Verified")



    def set_pin(self):
        if (len(self.pin)==4 or len(self.pin)==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pin_number")


def main():
    print("open_gpay")
    print("name_verification")
    print("mobile_verification")
    print("otp_verification")
    print("bank_verification")
    print("set_pin")

christy=Google_pay()
christy.open_gpay()
christy.name_verification()
christy.mobile_verification()
christy.otp_verf()
christy.bank_verification()
christy.set_pin()

    
