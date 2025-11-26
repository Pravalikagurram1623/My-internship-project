import numpy as np

def input_matrix(name):
    print(f"\nEnter details for matrix {name}:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    print(f"Enter the elements row by row, separated by spaces.")
    data = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        data.append(row)

    return np.array(data)

def print_matrix(title, m):
    print(f"\n{title}:")
    print(m)

def main():
    print("=== MATRIX OPERATIONS TOOL ===")

    # Input two matrices
    A = input_matrix("A")
    B = input_matrix("B")

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    while True:
        print("\nChoose an operation:")
        print("1. A + B (Addition)")
        print("2. A - B (Subtraction)")
        print("3. A x B (Multiplication)")
        print("4. Transpose of A or B")
        print("5. Determinant of A or B")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            if A.shape == B.shape:
                result = A + B
                print_matrix("A + B", result)
            else:
                print("\nAddition not possible: matrices must have same shape.")

        elif choice == "2":
            if A.shape == B.shape:
                result = A - B
                print_matrix("A - B", result)
            else:
                print("\nSubtraction not possible: matrices must have same shape.")

        elif choice == "3":
            if A.shape[1] == B.shape[0]:
                result = A @ B
                print_matrix("A x B", result)
            else:
                print("\nMultiplication not possible: columns of A must equal rows of B.")

        elif choice == "4":
            which = input("Transpose which matrix? (A/B): ").strip().upper()
            if which == "A":
                print_matrix("Transpose of A", A.T)
            elif which == "B":
                print_matrix("Transpose of B", B.T)
            else:
                print("Invalid choice, please type A or B.")

        elif choice == "5":
            which = input("Determinant of which matrix? (A/B): ").strip().upper()
            if which == "A":
                if A.shape[0] == A.shape[1]:
                    print(f"\nDeterminant of A: {np.linalg.det(A)}")
                else:
                    print("\nDeterminant not defined: A is not a square matrix.")
            elif which == "B":
                if B.shape[0] == B.shape[1]:
                    print(f"\nDeterminant of B: {np.linalg.det(B)}")
                else:
                    print("\nDeterminant not defined: B is not a square matrix.")
            else:
                print("Invalid choice, please type A or B.")

        elif choice == "6":
            print("\nExiting Matrix Operations Tool. Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()