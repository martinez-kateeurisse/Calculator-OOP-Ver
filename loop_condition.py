#This class file will include the codes for loop conditions.

from prog_design import ProgramDesign
prog_design = ProgramDesign()

#Create class
class LoopCondition:
#Create Object
    def retry_prog(self, retry):
    #Create variable instances(if-else condition)
        if retry == 'y':        
    #Return value
            return retry
        else:
            prog_design.program_footer()