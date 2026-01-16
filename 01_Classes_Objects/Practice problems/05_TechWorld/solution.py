class TechWorld:
    def __init__(self,name,technology,experience,feeback):
        self.__name = name
        self.__technologyskill = technology
        self.__experience = experience
        self.__avgfeedback = feeback
        
        
    def check_eligibility(self):
        if self.__experience >3 and self.__avgfeedback>=4.5 :
            return True 
        elif self.__experience <3 and self.__avgfeedback>=4:
            return True
        else :
            return False

    def allocate_course(self,subject):
        if self.check_eligibility():
            if subject in self.__technologyskill:
                print('course allocated')
            else:
                print('cannot allocate course')
        
p1 = TechWorld('sid',['Django','Machine Learning'],10,4.5)
p1.allocate_course('SpringBoot')

    



