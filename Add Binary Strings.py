class BinaryStringAdder:
    def add_binary_strings(self, s1: str, s2: str) -> str:
        num1 = int(s1, 2)  
        num2 = int(s2, 2)  
        result_sum = num1 + num2
        binary_result = bin(result_sum)[2:]
        return binary_result

if __name__ == "__main__":
    adder = BinaryStringAdder()
    s1 = "1101"  
    s2 = "111"   
    print(adder.add_binary_strings(s1, s2))  
    s1 = "00100"  
    s2 = "010"    
    print(adder.add_binary_strings(s1, s2))  
