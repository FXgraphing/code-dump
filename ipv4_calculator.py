# Input

octet1 = int(input("Enter the first octet (0-255): "))
octet2 = int(input("Enter the second octet (0-255): "))
octet3 = int(input("Enter the third octet (0-255): "))
octet4 = int(input("Enter the fourth octet (0-255): "))
prefix = int(input("Enter the prefix (0-32): "))

# Address count + actual host count math

address_count = 2 ** (32 - prefix)
host_count = address_count - 2

# Mask calculation, substracts address_count from the max 32 bit number

mask = (2 ** 32) - address_count
mask_octet1 = (mask >> 24) & 0xFF
mask_octet2 = (mask >> 16) & 0xFF
mask_octet3 = (mask >> 8) & 0xFF
mask_octet4 = mask & 0xFF

# Calculates the network address on each octet invidually by performing BITAND on the input octet and mask_octet

network_octet1 = octet1 & mask_octet1
network_octet2 = octet2 & mask_octet2
network_octet3 = octet3 & mask_octet3
network_octet4 = octet4 & mask_octet4

# Calculates the broadcast address on each octet invidually by performing BITOR on the network_octet and wildcard (inverted) mask

broadcast_octet1 = network_octet1 | (255 - mask_octet1)
broadcast_octet2 = network_octet2 | (255 - mask_octet2)
broadcast_octet3 = network_octet3 | (255 - mask_octet3)
broadcast_octet4 = network_octet4 | (255 - mask_octet4)

# Outputs the calculation results

print(f"IPv4: {octet1}.{octet2}.{octet3}.{octet4}/{prefix}")
print("============")
print(f"Network address: {network_octet1}.{network_octet2}.{network_octet3}.{network_octet4}")
print(f"Broadcast address: {broadcast_octet1}.{broadcast_octet2}.{broadcast_octet3}.{broadcast_octet4}")
print(f"Subnet mask: {mask_octet1}.{mask_octet2}.{mask_octet3}.{mask_octet4}")
print(f"Address count: {address_count}")
print(f"Host count: {host_count}")