#!/usr/bin/python3
from knock import KNOCKPY
from concurrent.futures import ThreadPoolExecutor
import os

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
    domain = 'google.com'
    file_path = "wordlist.txt"
    
    # Read the wordlist
    with open(file_path, "r") as f:
        buffer = f.read()

    # Split the buffer into 8 parts
    num_parts = 8
    buf_chunks = create_chunks(buffer, num_parts)

    # Write parts to files (optional)
    for i, chunk in enumerate(buf_chunks):
        with open(f"part_{i}.txt", "w") as part_file:
            part_file.write(chunk)

    # Start bruteforce using threads
    with ThreadPoolExecutor(max_workers=num_parts) as executor:
        for i, chunk in enumerate(buf_chunks):
            executor.submit(bruteforce, domain, chunk, i)

if __name__ == "__main__":
    main()
