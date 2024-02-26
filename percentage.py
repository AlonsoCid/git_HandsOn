import argparse

def nucleotide_percentage(sequence):
    sequence = sequence.upper()
    nucleotide_counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    
    if "U" in sequence:
        nucleotide_counts["U"] = 0
        del nucleotide_counts["T"]
    
    for nucleotide in sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
    
    total_nucleotides = sum(nucleotide_counts.values())
    nucleotide_percentages = {nucleotide: (count / total_nucleotides) * 100 for nucleotide, count in nucleotide_counts.items()}
    
    return nucleotide_percentages

def main():
    parser = argparse.ArgumentParser(description="Calculate the percentage of each nucleotide in a DNA or RNA sequence.")
    parser.add_argument('-s', '--sequence', type=str, required=True, help="The DNA or RNA sequence to analyze.")
    
    args = parser.parse_args()
    sequence = args.sequence
    
    percentages = nucleotide_percentage(sequence)
    for nucleotide, percentage in percentages.items():
        print(f"{nucleotide}: {percentage:.2f}%")

if __name__ == "__main__":
    main()

