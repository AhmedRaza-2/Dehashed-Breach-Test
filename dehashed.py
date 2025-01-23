import csv

def search_breached_data(query, csv_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            results = []
            for row in reader:
                if query.lower() in row['email'].lower() or query.lower() in row['username'].lower():
                    results.append(row)
            return results
    except FileNotFoundError:
        print("CSV file not found.")
        return []


def display_results(results):
    if results:
        print("\nBreached Data Found:")
        for result in results:
            print(f"Email: {result['email']}, Username: {result['username']}, Password: {result['password']}, Breach: {result['breach']}")
    else:
        print("No breached data found.")


def main():
    csv_file = 'dehashed.csv'  # Sample CSV file
    query = input("Enter email or username to search: ").strip()
    results = search_breached_data(query, csv_file)
    display_results(results)


if __name__ == "__main__":
    main()
