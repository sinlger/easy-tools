# A Toolio - Benchmark Builder User Guide

## Introduction
The Benchmark Builder is a simple yet handy online tool designed to help developers easily compare the execution time of different tasks, making it easier to optimize code performance.

## Features

### Benchmark Suite Management
- **Create Benchmark Suites**: You can create multiple benchmark suites to compare different tasks or scenarios.
- **Name Suites**: Each suite can be named for easy identification (e.g., "Original Algorithm" and "Optimized Algorithm").
- **Delete Suites**: Remove any suite that is no longer needed by clicking the delete option.

### Data Input
- **Enter Execution Times**: For each suite, input the execution time values of the task you want to benchmark.
- **Add More Values**: Click "Add a measure" to include more data points, which helps in improving the accuracy and reliability of the benchmark results.
- **Remove Values**: If you enter a wrong value or identify an outlier, you can delete individual values using the trash can icon next to them.

### Unit Configuration
- **Set Time Unit**: Specify the unit of time (e.g., ms for milliseconds) that the execution times are measured in. This ensures all results are presented in a consistent and understandable format.

### Results Display and Analysis
- **Result Table**: After inputting data, the tool displays the results in a clear table format.
- **Key Metrics**: The table includes important metrics such as position (ranking based on mean execution time), suite name, number of samples, mean execution time, and variance (a measure of how much the execution times vary).
- **Comparison**: The results table allows for easy comparison of different suites. For example, it shows how much faster one suite is compared to another in terms of both absolute time difference and percentage.

### Results Export
- **Copy as Markdown Table**: This option allows you to copy the results in Markdown format, which is useful for including the results in documentation or reports that support Markdown.
- **Copy as Bullet List**: You can also copy the results as a bullet list, which is helpful for presenting the information in a different format that might be more suitable for certain types of documents or presentations.

## Usage Example
1. **Setup**: Begin by creating two benchmark suites, one for the original version of your function and another for the optimized version.
2. **Data Collection**: Run both versions of your function multiple times and record the execution times. It is recommended to collect at least several samples for each suite to ensure statistical significance.
3. **Input Data**: Enter the recorded execution times into the respective suites in the Benchmark Builder.
4. **Set Unit**: Specify the appropriate time unit (e.g., ms) to ensure the results are displayed correctly.
5. **Analyze Results**: View the results table to compare the performance of the two versions. Pay attention to the mean execution time and variance to understand both the speed and consistency of each version.
6. **Export Results**: Use the export options to include the results in your technical documentation or performance reports.

## Conclusion
The A Toolio - Benchmark Builder provides a straightforward and efficient way to benchmark and compare the performance of different code implementations. By following this guide, you can effectively utilize the tool to make data-driven decisions for optimizing your code and improving application performance.