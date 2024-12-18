import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Subdomain Scanner Tool - A simple subdomain brute-force tool."
    )

    # Thêm các tùy chọn (options)
    parser.add_argument("--version", action="version", version="1.0", help="Show program's version number and exit")
    parser.add_argument("-f", metavar="FILE", type=str, default="subnames.txt",
                        help="File contains new line delimited subs, default is subnames.txt.")
    parser.add_argument("--full", action="store_true",
                        help="Full scan, NAMES FILE subnames_full.txt will be used to brute.")
    parser.add_argument("-i", "--ignore-intranet", action="store_true",
                        help="Ignore domains pointed to private IPs.")
    parser.add_argument("-w", "--wildcard", action="store_true",
                        help="Force scan after wildcard test failed.")
    parser.add_argument("-t", "--threads", type=int, default=500,
                        help="Number of scan threads, 500 by default.")
    parser.add_argument("-p", "--process", type=int, default=6,
                        help="Number of scan processes, 6 by default.")
    parser.add_argument("--no-https", action="store_true",
                        help="Disable getting domain names from HTTPS cert, saving some time.")
    parser.add_argument("-o", "--output", type=str,
                        help="Output file name, default is {target}.txt.")

    # Thêm target domain (bắt buộc)
    parser.add_argument("target", metavar="target.com", type=str,
                        help="Target domain to scan for subdomains.")

    # Phân tích các tham số dòng lệnh
    args = parser.parse_args()

    # Hiển thị các giá trị được nhập
    print("Target Domain:", args.target)
    print("Options:")
    print(" - File:", args.f)
    print(" - Full Scan:", args.full)
    print(" - Ignore Intranet:", args.ignore_intranet)
    print(" - Wildcard:", args.wildcard)
    print(" - Threads:", args.threads)
    print(" - Processes:", args.process)
    print(" - No HTTPS:", args.no_https)
    print(" - Output:", args.output)

    # Thực hiện các hành động dựa trên tham số
    # Ví dụ:
    if args.full:
        print("Performing full scan...")
    if args.ignore_intranet:
        print("Ignoring private IPs...")

    # Kết thúc chương trình
    print("Scanning subdomains for", args.target, "...")
    # Thêm logic quét subdomain ở đây

if __name__ == "__main__":
    main()
