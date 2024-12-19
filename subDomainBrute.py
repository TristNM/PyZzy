#!/usr/bin/python3
from knock import KNOCKPY
from concurrent.futures import ThreadPoolExecutor
import os
import argparse

def create_chunks(buffer, num_parts):
    chunk_size = len(buffer) // num_parts
    chunks = [buffer[i:i + chunk_size] for i in range(0, len(buffer), chunk_size)]
    if len(buffer) % num_parts != 0:  # Add remaining part
        chunks[-1] += buffer[num_parts * chunk_size:]
    return chunks

def bruteforce(domain, file_content, num):
    print(f"Thread_{num} started...")
    try:
        results = KNOCKPY(domain, dns=None, useragent=None, timeout=None, threads=None, recon=True, bruteforce=True, wordlist=file_content.splitlines())
        with open(f"result_{num}.txt", "w") as f:
            f.write(str(results))
        print(f"Thread_{num} completed.")
    except Exception as e:
        print(f"Thread_{num} encountered an error: {e}")

def main():
    # Set up argparse
    parser = argparse.ArgumentParser(description="Bruteforce subdomains using KNOCKPY")
    parser.add_argument("-u", "--domain", required=True, help="Target domain for bruteforce")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-t", "--threads", type=int, default=8, help="Number of threads to use (default: 8)")
    parser.add_argument("-o", "--output", default="results", help="Output directory for results (default: ./results)")

    args = parser.parse_args()

    # Parse arguments
    domain = args.domain
    file_path = args.wordlist
    num_parts = args.threads
    output_dir = args.output

    # Create output directory if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the wordlist
    with open(file_path, "r") as f:
        buffer = f.read()

    # Split the buffer into parts
    buf_chunks = create_chunks(buffer, num_parts)

    # Write parts to files (optional)
    for i, chunk in enumerate(buf_chunks):
        with open(os.path.join(output_dir, f"part_{i}.txt"), "w") as part_file:
            part_file.write(chunk)

    # Start bruteforce using threads
    with ThreadPoolExecutor(max_workers=num_parts) as executor:
        for i, chunk in enumerate(buf_chunks):
            executor.submit(bruteforce, domain, chunk, i)

if __name__ == "__main__":
    main()
