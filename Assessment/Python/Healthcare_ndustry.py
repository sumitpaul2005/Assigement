class BookAppointment:
    def __init__(self):
        self.appointment = {}
        self.slot = ["10am","11am","12pm","2pm","3pm"]
        
    def patientDetails(self):
        name = input("Enter the patient name : ")
        age = int(input("Enter your age : "))
        
        ph = input("Enter your mobile number : ")   
        if ph.isdigit() and len(ph) == 10:          
            mobile = ph
        else:
            print("Please enter 10 digit number!!")
            return
        
        doctor_name = input("Enter the Doctor name : ")
        
        print("Available Slot!!")
        for i in self.slot:
            print(i)
            
        slot = input("Enter Slot from given slot : ")
        
        count = 0
        for i in self.appointment.values():
            if i["doctor_name"] == doctor_name and i["slot"] == slot:
                count += 1
                
        if count < 3:
            self.appointment[mobile] = {
                "name": name,
                "age": age,
                "doctor_name": doctor_name,
                "slot": slot
            }
            print("Appointment Booked Successfully!!")
        else:
            print("Selected Slot is full for this doctor!!")
        
    def View_Appointment(self):
        if len(self.appointment) == 0:
            print("First Book Appointment!!")
            return 
        
        ph = input("Enter your mobile number : ")   
        
        if ph in self.appointment:
            print("Patient Details : ")
            print(self.appointment[ph])
        else:
            print("Details not found!!")
            
    def Cancel_Appointment(self):
        if len(self.appointment) == 0:
            print("First Book Appointment!!")
            return 
        
        ph = input("Enter your mobile number : ")   
        
        if ph in self.appointment:
            del self.appointment[ph]
            print("Cancellation Successfully")
        else:
            print("Records not found!!")
    
    def InputDetails(self):
        while True:
            menu = """
                Press 1 : Booked Appointment
                Press 2 : View Details
                Press 3 : Cancel Appointment
                Press 4 : Exit
            """
            print(menu)
            
            try:
                n = int(input("Enter your choices : "))   
            except:
                print("Invalid input!")
                continue
            
            if n == 1:
                self.patientDetails()
            elif n == 2:
                self.View_Appointment()
            elif n == 3:
                self.Cancel_Appointment()
            elif n == 4:
                print("Thank you!!")
                break
            else:
                print("Invalid Choices!!")


obj = BookAppointment()
obj.InputDetails()