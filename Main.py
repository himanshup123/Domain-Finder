import requests

def domain_scanner(domain_name, sub_domnames):
    print("----URLs after scanning subdomains----")
    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(url)
        except requests.ConnectionError:
            pass

def main():
    domain_name = input("Enter the domain name (e.g., example.com): ")
    with open("subdomains.txt", "r") as file:
        sub_domnames = file.read().splitlines()
    domain_scanner(domain_name, sub_domnames)

if __name__ == "__main__":
    main()
