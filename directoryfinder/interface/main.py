import requests
import sys

def scan_directory(base_url, directories):
    print(f"Start Scanning: {base_url}")

    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = "https://" + base_url

    # Create a filename based on the website
    domain_name = base_url.replace("http://", "").replace("https://", "").replace("/", "_")
    results_file = f"{domain_name}_results.txt"

    try:
        base_response = requests.get(base_url, timeout=5)
        base_length = len(base_response.text)
        print(f"[INFO] Base page length: {base_length}")
    except requests.RequestException as e:
        print(f"[ERROR] Could not connect to {base_url}: {e}")
        sys.exit(1)

    with open(results_file, "w") as result:
        result.write(f"Scan Results for {base_url}\n")
        result.write("=" * 40 + "\n")

        for directory in directories:
            directory = directory.strip()
            url = f"{base_url}/{directory.strip()}"
            try:
                response = requests.get(url, timeout=5)
                response_length = len(response.text)

                if response.status_code == 200 and response_length != base_length:
                    output = f"[FOUND] {url} - Status: {response.status_code} (Length: {response_length})"

                elif response_length == base_length:
                    output = f"[FAKE] {url} - Matches Base Page (Status: {response.status_code})"

                else:
                    output = f"[NOT FOUND] {url} - Status: {response.status_code}"
            except requests.RequestException as e:
                output = f"[ERROR] {url} - {e}"

            print(output)  # Print to console
            result.write(output + "\n")  # Save to file

    print(f"\nResults saved to: {results_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with open("directory.txt", "r") as f:
            directories = f.readlines()
    except FileNotFoundError:
        print("Error: 'directory.txt' not found.")
        sys.exit(1)

    scan_directory(url, directories)