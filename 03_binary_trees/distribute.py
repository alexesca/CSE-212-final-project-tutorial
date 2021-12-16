from tree import BST

def main():
    bt = BST()
    alphabet = {
        'A': "00",
        'B': "1",
        'C': "011",
        'D': "010",
    }
    bt.distribute(alphabet)
    for x in bt:
        print(x)

if __name__ == "__main__":
    main()
