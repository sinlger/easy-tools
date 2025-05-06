# IPv4 Range Expander User Guide

## I. Tool Introduction

The IPv4 Range Expander calculates a valid IPv4 network, including the netblock (in CIDR notation), address range, and the number of addresses within the range, based on the inputted start and end IPv4 addresses.

## II. Feature Details

### (I) Basic Input Function

  1. **Start Address Input**: Enter the starting IPv4 address in the "Start address" box, e.g., "192.168.1.1".
  2. **End Address Input**: Enter the ending IPv4 address in the "End address" box, e.g., "192.168.6.255".

### (II) Automatic Processing and Result Display

  1. **Address Range Adjustment**: The tool automatically adjusts the start and end addresses to a more suitable range. For example, "192.168.1.1" is adjusted to "192.168.0.0" and "192.168.6.255" to "192.168.7.255".
  2. **Address Count Calculation**: It calculates the number of IPv4 addresses in the new range, such as adjusting from "1,535" to "2,048" for more efficient address resource utilization.
  3. **CIDR Notation Generation**: Provides the CIDR notation corresponding to the new address range, e.g., "192.168.0.0/21", facilitating network management and configuration.

## III. Notes

Ensure the inputted start and end addresses are in the correct IPv4 address format to guarantee the tool's proper operation and result accuracy.