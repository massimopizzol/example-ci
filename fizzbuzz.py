def fizzbuzz(int_arg):

    if int_arg % 3 == 0 and int_arg % 5 == 0:
        return "fizzbuzz"
    if int_arg % 3 == 0 :
        return "fizz" 
    if int_arg % 5 == 0 :
        return "buzz"
    if int_arg < 1:
        raise ValueError()


def test_fizzbuzz1():
    
    assert fizzbuzz(9) == "fizz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(15) == "fizzbuzz"
    
def test_fizzbuzz2():

    from pytest import raises    

    with raises(ValueError):
          fizzbuzz(0.1)
   
