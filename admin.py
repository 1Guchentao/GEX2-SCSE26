import json

def load_library(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_library(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def find_book(books, search_text):
    search_text = search_text.strip().lower()
    
    for book_id, book in books.items():
        if book_id.lower() == search_text:
            return book_id
            
    for book_id, book in books.items():
        if search_text in book["title"].lower() or search_text in book["author"].lower():
            return book_id
            
    return None

def display_books(books):
    print("BOOK CATALOGUE")
    print("-" * 60)
    for book_id, book in books.items():
        availability = "AVAILABLE" if book["available"] else "ON LOAN"
        print(f"{book_id} | {book['title']} | {book['category']} | {availability}")

def display_loans(loans, books):
    print("CURRENT LOANS")
    print("-" * 60)
    for loan in loans:
        book_id = loan["book_id"]
        title = books.get(book_id, {}).get("title", "Unknown")
        print(f"{book_id} | {title} | Borrower: {loan['borrower']}")

def library_statistics(books):
    total = len(books)
    available = sum(1 for book in books.values() if book["available"])
    borrowed = total - available
    return (total, available, borrowed)

def main():
    data = load_library("library.json")
    
    print("LIBRARY ADMINISTRATION")
    print("=" * 60)
    print(f"Library: {data['library']['name']}")
    print(f"Branch: {data['library']['branch']}")
    print(f"Year: {data['library']['year']}")
    print(f"Categories: {', '.join(data['categories'])}\n")
    
    display_books(data["books"])
    print("\n")
    
    display_loans(data["loans"], data["books"])
    print("\n")
    
    stats = library_statistics(data["books"])
    print("STATISTICS")
    print("-" * 60)
    print(f"Total books: {stats[0]}")
    print(f"Available: {stats[1]}")
    print(f"Borrowed: {stats[2]}")

if __name__ == "__main__":
    main()
""" 
LIBRARY ADMINISTRATION
============================================================
Library: 
Branch: 
Year: 
Categories: 

BOOK CATALOGUE
------------------------------------------------------------
ID1 | Title1 | Category | Availability
ID2 | Title2 | Category | Availability
...
...
...
IDN | TitleN | Category | Availability


CURRENT LOANS
------------------------------------------------------------
ID1 | Title1 | Borrower: Borrower1
ID2 | Title2 | Borrower: Borrower2
...
...
...
IDN | TitleN | Borrower: BorrowerN

STATISTICS
------------------------------------------------------------
Total books: XX
Available: XX
Borrowed: XX
"""