def test_prime_num_generator():
    expected_first_12_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    expected_101st_prime = 547

    
    primes = prime_num_generator(12)
    assert primes == expected_first_12_primes, f"Expected {expected_first_12_primes}, but got {primes}"

   
    prime_101 = prime_num_generator(101)
    assert prime_101 == expected_101st_prime, f"Expected {expected_101st_prime}, but got {prime_101}"
    
    ########################################################
    
    def test_palindrom():
    
    assert palindrom("") == False, "Expected False for empty argument"
    
    assert palindrom(12345) == False, "Expected False for non-string argument"
    
    assert palindrom("hello world") == False, "Expected False for text without palindromic words"
    
    assert palindrom("level radar civic") == True, "Expected True for text with palindromic words with even number of letters"
    
    assert palindrom("deed racecar kayak") == True, "Expected True for text with palindromic words with odd number of letters"
    
    ########################################################
    
    def test_validate_ip():
    
    assert validate_ip("") == False, "Expected False for empty argument"

    assert validate_ip(12345) == False, "Expected False for non-string argument"

    assert validate_ip("192.168.0.256") == False, "Expected False for invalid IP address format"

    assert validate_ip("192.168.0.1") == True, "Expected True for valid IP address format"
    
    #######################################################
    
    def test_get_os(self):
        self.assertIn(get_os('Windows'), ['Windows 10', 'Windows 7', 'Windows 8']) 
        self.assertIn(get_os('macOS'), ['macOS Big Sur', 'macOS Catalina', 'macOS Mojave']) 
        self.assertIn(get_os('Linux'), ['Ubuntu', 'Debian', 'Fedora']) 
