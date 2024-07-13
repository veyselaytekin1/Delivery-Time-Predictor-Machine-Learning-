import os, sys

class CustomException(Exception): # a built python function to get detail of error
    def __init__(self, error_message: Exception, error_details:sys):
        self.error_message = CustomException.get_detailed_error_message(
                                                                        error_message=error_message,
                                                                        error_details=error_details)
        


    
    @staticmethod  # independent from class
    def get_detailed_error_message(error_message:Exception, error_detailes: sys)->str:
        _, _, exce_tb = error_detailes.exc_info()

        exception_block_line_number = exce_tb.tb_frame.f_lineo
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename  # get detail pf error


        error_message = f"""
        Error occured in execution of :
        [{file_name}] at 
        try block line number : [{try_block_line_number}]
        error message : [{error_message}]
        
        """ # the error message
        return error_message


    def __str__(self):  # that give the message to user like print function
        return self.error_message

    def __repr__(self): 
        return CustomException.__name__.str()
