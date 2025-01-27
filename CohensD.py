# This script calculates the effect size Cohen's d
# when in a two group experiment, the two sample sizes (n1 & n2),
# the two means (m1 & M2) and the corresponding standard deviations (SD1 & SD2) are known
# The calculation is based on Cohen's d formula in 
# A short statement interepreting the calculated value is also provided.
# Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Hillsdale, NJ: Erlbaum.


import math


def calculate_cohens_d(M1, M2, SD1, SD2, n1, n2):
    # Calculate the mean difference
    mean_difference = M1 - M2

    # Calculate the pooled standard deviation
    SD_pooled = math.sqrt(((n1 - 1) * SD1**2 + (n2 - 1) * SD2**2) / (n1 + n2 - 2))

    # Calculate Cohen's d
    cohens_d = mean_difference / SD_pooled

    return cohens_d

def interpret_cohens_d(d):
    if d < 0.2:
        return "The calculated effect size indicates a very small effect"
    elif 0.2 <= d < 0.5:
        return "The calculated effect size indicates a small effect"
    elif 0.5 <= d < 0.8:
        return "The calculated effect size indicates a medium effect"
    else:
        return "The calculated effect size indicates a large effect"

# Get user input for the values
M1 = float(input("Enter the mean of the experimental group or Group 1 (M1): "))
M2 = float(input("Enter the mean of the control group or Group 2 (M2): "))
SD1 = float(input("Enter the standard deviation of experimental group or Group 1 (SD1): "))
SD2 = float(input("Enter the standard deviation of control group or Group 2 (SD2): "))
n1 = int(input("Enter the sample size of experimental group or Group 1 (n1): "))
n2 = int(input("Enter the sample size of control group or Group 2 (n2): "))

# Calculate Cohen's d
cohens_d = calculate_cohens_d(M1, M2, SD1, SD2, n1, n2)

print(f"Cohen's d is {cohens_d:.2f}")

# Interpret Cohen's d
print(interpret_cohens_d(cohens_d))

print("Ref:Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Hillsdale, NJ: Erlbaum.")

