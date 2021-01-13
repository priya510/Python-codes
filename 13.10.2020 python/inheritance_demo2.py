

class Employee:
    wh=0
    
    def showWorkingHours(self):
        print("Working Hours: ",self.wh)


class PartTimeEmployee(Employee):
    wh=4
    
    def showWorkingHours(self):
        super().showWorkingHours()


class FullTimeEmployee(Employee):
    wh=8
    
    def showWorkingHours(self):
        super().showWorkingHours()


pte=PartTimeEmployee()
fte=FullTimeEmployee()

pte.showWorkingHours()
fte.showWorkingHours()
