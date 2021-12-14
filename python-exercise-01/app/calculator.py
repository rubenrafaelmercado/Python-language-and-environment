

def calculator ( number1, number2, operation ):

    # improvement to refactor: merge operations and results
    
    operations = [ "+", "-", "/", "*" ]

    results = {
        '+': number1 + number2,
        '-': number1 - number2,
        '/': number1 / number2,
        '*': number1 * number2,    
    }

    if operations.__contains__(operation):
        return ( results[operation] )
    else:
        return ( 'not valid operation' )

    