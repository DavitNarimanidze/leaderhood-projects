def non_prime(start , end):
    non_primes = []
    # გადავუვლი ყველა რიცხვს start,end შუალედში 
    for i in range(start, end + 1):
        # თუ რიცხვი ნაკლებია ან ტოლი 1 ის ის არ არის PRIME  
        if i <= 1:
            non_primes.append(i) # ამატებს სიაში რიცხვს რომელიც 1ზე ნაკლებია ან თანაბარი 
        else:
            is_prime = True
            # შევამოწმებთ თუ რიცხვი იყოა 2 და num შორის 
            for ia in range(2, int(i ** 0.5) + 1):
                # თუ რიცხვი იყოფა Iზე არ არის prime 
                if i % ia == 0:
                    is_prime = False
                    break #შემოწმებას აღარ ვაგრძელევთ

            # თუ რიცხვი არ არის PRIME სიაში ვამატებთ 
            if not is_prime:
                non_primes.append(i)

    return non_primes

print(non_prime(start = 10, end = 20))
print(non_prime(start = 1, end = 10))
print(non_prime(start = 20, end = 30))
print(non_prime(start = 24, end = 25))
print(non_prime(start = 1, end = 1))