import datetime
import simulation
import utility

class subject:

    def __init__(self, weight, height, dob ):
        self.weight = weight
        self.height = height
        self.dob    = datetime.datetime.strptime(dob, "%d/%m/%Y")
        self.__updateBMR()

    def __str__(self):
        return "Age: " + str(self.GetAge()) + "\n"\
               "Age Years: " + str(self.GetAgeYears()) + "\n" \
               "Weight: " + str(self.GetWeight()) + "Kg\n" + \
               "BMR: " + str(self.GetBMR()) + "kcal\n" \
               "Height: " + str(self.GetHeight()) + "cm\n"

    def GetAge(self):
        return simulation.clock.now() - self.dob
    
    def GetAgeYears(self):
        now = simulation.clock.now()
        return now.year - self.dob.year - ((now.month, now.day) < (self.dob.month, self.dob.day))
    
    def GetWeight(self):
        return self.weight
    
    def GetHeight(self):
        return self.height
    
    def GetBMR(self):
        return self.bmr
    
    def __updateBMR(self):
        bmr = 66.47 + (13.75 * self.GetWeight()) + (5.003 * self.GetHeight()) - (6.755 * self.GetAgeYears())
        bmr = bmr*1.2
        self.bmr=bmr
    
    def __updateWeight(self,time_delta, kcal_consumed):
        kcal_burned = self.GetBMR() * (time_delta/datetime.timedelta(days=1))
        kcal_delta = kcal_consumed - kcal_burned
        self.weight += utility.CaloriesToKilos(kcal_delta)

    def Update(self,time_delta,kcal_consumed):
        self.__updateBMR()
        self.__updateWeight(time_delta, kcal_consumed)