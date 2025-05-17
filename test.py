import argparse

def parse_ports(value):
    ports = []
    seen = set()

    for part in value.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            #if start > end:
                #raise argparse.ArgumentTypeError(f"Invalid range: {part}")
            for port in range(start, end + 1):
                #if port in seen:
                    #raise argparse.ArgumentTypeError(f"Duplicate port detected: {port}")
                seen.add(port)
                ports.append(port)
        else:
            port = int(part)
            #if port in seen:
                #raise argparse.ArgumentTypeError(f"Duplicate port detected: {port}")
            seen.add(port)
            ports.append(port)

    return ports
print(parse_ports("80-400,333,24"))