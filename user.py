from admin import load_library, save_library, find_book

def books_in_category(books, category):
    target = category.strip().lower()
    return [
        book_id for book_id, book in books.items() 
        if book["category"].lower() == target
    ]

def search_by_title(books, search_text):
    target = search_text.strip().lower()
    return [
        book_id for book_id, book in books.items() 
        if target in book["title"].lower()
    ]

def borrow_book(books, loans, search_text, borrower):
    book_id = find_book(books, search_text)
    if not book_id:
        return "BOOK_NOT_FOUND"
    
    b_name = borrower.strip()
    if not b_name:
        return "EMPTY_NAME"
        
    if not books[book_id]["available"]:
        return "NOT_AVAILABLE"
        
    books[book_id]["available"] = False
    loans.append({"book_id": book_id, "borrower": b_name})
    
    return "OK"

def return_book(books, loans, book_title, borrower):
    book_id = find_book(books, book_title)
    if not book_id:
        return "BOOK_NOT_FOUND"
        
    b_name = borrower.strip()
    if not b_name:
        return "EMPTY_NAME"
        
    if books[book_id]["available"]:
        return "NOT_ON_LOAN"
        
    books[book_id]["available"] = True
    
    for i in range(len(loans)):
        if loans[i]["book_id"] == book_id and loans[i]["borrower"] == b_name:
            loans.pop(i)
            break
    else:
        for i in range(len(loans)):
            if loans[i]["book_id"] == book_id:
                loans.pop(i)
                break
                
    return "OK"

def main():
    data = load_library("library.json")
    
    while True:
        print("\nLIBRARY USER SYSTEM")
        print("1. Search by Category")
        print("2. Search by Title")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            cat = input("Enter category: ")
            results = books_in_category(data["books"], cat)
            print(f"Found books: {results}")
            
        elif choice == "2":
            title = input("Enter title: ")
            results = search_by_title(data["books"], title)
            print(f"Found books: {results}")
            
        elif choice == "3":
            search_text = input("Enter book ID, Title, or Author: ")
            borrower = input("Enter your name: ")
            res = borrow_book(data["books"], data["loans"], search_text, borrower)
            print(res)
            
        elif choice == "4":
            search_text = input("Enter book ID, Title, or Author: ")
            borrower = input("Enter your name: ")
            res = return_book(data["books"], data["loans"], search_text, borrower)
            print(res)
            
        elif choice == "5":
            save_library(data, "library.json")
            break
            
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()