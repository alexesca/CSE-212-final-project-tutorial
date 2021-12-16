# Factorization solution

    from tree import BST


    def recursive_factorization(n, i, bt):
        if i > n:
            return
        reminder = n % i
        is_factor = reminder == 0
        if is_factor:
            bt.insert(i)
        recursive_factorization(n, i+1, bt)
    
    
    def factor_number(n, bt):
        recursive_factorization(n, 1, bt)
    
    
    if __name__ == "__main__":
        bt = BST()
        factor_number(12, bt)
        for factor in bt:
            print(factor)


[Here](factorization.py) is the python file.
