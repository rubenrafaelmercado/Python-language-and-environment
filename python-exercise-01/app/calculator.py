

def calculator ( number1, number2, operation ):

    operations = ['+','-','/','*',]
    
    if operations.__contains__(operation):
        
        calculation = str(number1) +  operation + str(number2)
                
        return ( eval(calculation) )
    else:
        return ( 'not valid operation' )

    