# Complaint Classification System - Day 2 MVP

from rules import classify_complaint


def main():
    complaint = input("Enter your complaint: ")

    category = classify_complaint(complaint)

    print(f"\nCategory: {category}")


if __name__ == "__main__":
    main()
