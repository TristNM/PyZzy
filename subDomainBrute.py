import argparse
import requests
import sys
import os

def Scan(url, wordlist):
    # if not url.startswith("http://") and not url.startswith("https://"):
    #     url = "https://" + url

    # # Đọc wordlist
    # try:
    #     with open(wordlist, "r") as file:
    #         subdomains = file.readlines()
    # except FileNotFoundError:
    #     print(f"Không tìm thấy file wordlist: {wordlist}")
    #     return

    # for subdomain in subdomains:
    #     subdomain = subdomain.strip()  # loại bỏ khoảng trắng thừa và ký tự newline
    #     full_url = f"{url}/{subdomain}"
    #     try:
    #         req = requests.get(full_url)

    #         if req.status_code == 200:
    #             print(f"[+] {full_url} - {req.status_code} OK")
    #             req.encoding = 'utf-8'
    #             print(req.text[:200])  # In ra 200 ký tự đầu tiên của nội dung trả về
    #         else:
    #             print(f"[-] {full_url} - {req.status_code}")
    #     except requests.exceptions.RequestException as e:
    #         print(f"Lỗi khi thực hiện yêu cầu với {full_url}: {e}")
    discovered = []  
    try:
        with open(wordlist, 'r') as file:
            subdomains = file.read().splitlines()
        
        for subdomain in subdomains:
            url = "https://{}.{}".format(subdomain, url)
            try:
                print("T")
                response = requests.get(url)
                if response.status_code == 200:
                    discovered.append(url)
            except requests.exceptions.RequestException:
                pass
    
    except FileNotFoundError:
        print(f"Không tìm thấy file wordlist: {wordlist}")
    return discovered

def main():
    parser = argparse.ArgumentParser(
        description="Subdomain Scanner Tool - A simple subdomain brute-force tool with HTTP request support."
    )

    # Options
    parser.add_argument("--version", action="version", version="1.0", help="Show program's version number and exit")
    parser.add_argument("-f", metavar="FILE", type=str, default="subnames.txt",
                        help="File contains new line delimited subs, default is subnames.txt.")
    parser.add_argument("--full", action="store_true",
                        help="Full scan, NAMES FILE subnames_full.txt will be used to brute.")
    parser.add_argument("-i", "--ignore-intranet", action="store_true",
                        help="Ignore domains pointed to private IPs.")
    parser.add_argument("-w", "--wordlist", type=str, default="wordlist.txt",
                        help="Path to the wordlist file for subdomain scanning. Default is wordlist.txt.")
    parser.add_argument("-t", "--threads", type=int, default=500,
                        help="Number of scan threads, 500 by default.")
    parser.add_argument("-p", "--process", type=int, default=6,
                        help="Number of scan processes, 6 by default.")
    parser.add_argument("--no-https", action="store_true",
                        help="Disable getting domain names from HTTPS cert, saving some time.")
    parser.add_argument("-o", "--output", type=str,
                        help="Output file name, default is {target}.txt.")
    parser.add_argument("-u", type=str, required=True,
                        help="Send HTTP GET request to the specified URL.")
    parser.add_argument("target", metavar="target.com", type=str, nargs="?",
                        help="Target domain to scan for subdomains.")

    args = parser.parse_args()

    print("Target Domain:", args.target)
    print("Options:")
    print(" - File:", args.f)
    print(" - Full Scan:", args.full)
    print(" - Ignore Intranet:", args.ignore_intranet)
    print(" - Wordlist:", args.wordlist)
    print(" - Threads:", args.threads)
    print(" - Processes:", args.process)
    print(" - No HTTPS:", args.no_https)
    print(" - Output:", args.output)

    print("Debug: args.url =", args.u)

    if args.u:
        print("Performing HTTP GET request to:", args.u)
        # Kiểm tra nếu user cung cấp wordlist, nếu không dùng mặc định
        wordlist_path = args.wordlist if os.path.exists(args.wordlist) else "wordlist.txt"
        print("Using wordlist:", wordlist_path)
        Scan(args.u, wordlist_path)

if __name__ == "__main__":
    main()
