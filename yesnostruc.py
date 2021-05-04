solution_dict = {
    "I may be able to assist! Please see possible solution below<br>Cause:AC mains may not be connected or battery too low<br> Solution:Check that AC mains is properly connected to outlet or battery capacity is sufficient.<br> Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!": "code1",
    
    "I'm sorry to hear that. Please see possible solution below<br>Cause:cable may be defective<br>Solution:Check that the cable between the keypad board and main board is correctly connected. Please reference the service manual for steps to open device and verify this.<br>Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!" : "code2",
    
    "I'm sorry to hear that. Please see possible solution below<br>Cause:cable may be defective<br>Solution:Check that the cable between the power board and power management board is correctly connected.<br>Please reference the service manual for steps to open device and verify this.<br>Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!":"code3",
    
    "I'm sorry to hear that. Please see possible solution below<br>Cause:cable may be defective<br>Check that the cable between the main board and power management board is correctly connected.<br>Please reference the service manual for steps to open device and verify this.<br>Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!":"code4",
    
    "I'm sorry to hear that. Please see possible solution below<br>Cause:Power board may be defective<br> Solution:Replace the power board.<br>Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!":"code5",
    
    "I'm sorry to hear that. Please see possible solution below<br>Cause:Power management board may be defective<br>Solution:Replace the power management board.<br>Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!":"code6",

    "I'm sorry to hear that. Please see possible solution below<br>Cause:The main board failed<br> Solution:Replace the main board.<br>Please give this a try, and respond with 'worked' or 'did not work' if this helped, and we'll proceed from there!":"code7",
    
    }

solution_dict =  {k.lower(): v for k, v in solution_dict.items()}
