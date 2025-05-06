# IPv6 ULA Generator User Manual

## I. Tool Introduction

The IPv6 ULA Generator is an online tool that helps users generate IPv6 addresses that are local and not routable over the internet, in line with RFC4193 standards.It is useful for creating unique network identifiers within a local area network (LAN).

## II. Main Features

  1. **Generation of Random ULA Based on Multiple Factors**

     * This tool uses the first method recommended by IETF.It combines the current timestamp and MAC address, applies the SHA1 hash algorithm, and takes the lower 40 bits to generate a random ULA.This ensures the generated address has high randomness and uniqueness, reducing the risk of address conflicts and providing reliable local network identification for devices within a LAN.

  2. **MAC Address Input and Processing**

     * Users can manually input a MAC address in the designated box in the standard format (e.g., "20:37:06:12:34:56").The tool uses this MAC address as a key parameter in calculating the ULA address.

  3. **Generation of ULA Address and Routing Block Information**

     * **IPv6 ULA** :The tool generates a full IPv6 ULA address starting with "fd", in line with the RFC4193 format.For example, "fd1d:dba9:6f7b::/48" indicates the prefix length is 48 bits, offering a unique network identifier for LAN devices for configuration and communication.
     * **First routable block** :It generates the first routable block address, such as "fd1d:dba9:6f7b:0::/64", showing the starting range of allocable addresses within the ULA range.This helps users plan and allocate network addresses.
     * **Last routable block** :It generates the last routable block address, like "fd1d:dba9:6f7b:ffff::/64", indicating the ending range of allocable addresses within the ULA range.This provides users with complete information on the available address range for network deployment and device configuration.

## III. Use Cases

  1. In enterprise LANs, assign unique local IPv6 addresses to devices to avoid conflicts with global IPv6 addresses while ensuring internal communication.
  2. In network testing environments, generate local non - routable ULA addresses to simulate scenarios for testing network devices and applications without using official IPv6 addresses.
  3. In home networks, assign ULA addresses to routers and smart devices to enhance stability and security and prevent external unauthorized access.

## IV. How to Use

  1. Visit the online URL of the IPv6 ULA Generator:[https://it - tools.tech/ipv6 - ula - generator](https://it-tools.tech/ipv6-ula-generator).
  2. If you know the device's MAC address, input it in the standard format in the "MAC address" box.If not, the tool may use a default or randomly generated MAC address.
  3. Click the "Generate" button.The tool will calculate and generate the corresponding IPv6 ULA address, first routable block address, and last routable block address based on the input MAC address (or default) and current timestamp.
  4. View the generated address information and apply it to device configuration, network planning, or testing as needed.

## V. Notes

  1. ULA addresses are for LAN use only and cannot be routed over the internet.For internet communication, devices still need globally routable IPv6 addresses.
  2. Ensure the input MAC address is accurate to avoid network configuration issues due to incorrect ULA addresses.
  3. Maintain the uniqueness of ULA addresses within the LAN to prevent conflicts that could disrupt device communication.