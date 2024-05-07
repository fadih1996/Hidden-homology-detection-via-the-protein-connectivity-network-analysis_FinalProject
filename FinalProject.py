# Function to read sequences from a FASTA file
import os
import tkinter as tk

def read_fasta(file_path):
    sequences = []

    import os
    # assign directory
    # iterate over files in
    # that directory
    f = file_path
    # checking if it is a file
    if os.path.isfile(f):
        with open(f, 'r') as file:
            sequence = ''
            header=''
            for line in file:
                if '>' in line:  # Header line
                    #if line.endswith('SV=1'):
                    if sequences or sequence:
                        sequences.append(sequence)
                    header += line.strip()
                    sequence = ''
                    sequence += header + "\n"
                    header = ''
                else:
                    sequence += line.strip()
            if sequence:  # Add the last sequence
                sequences.append(header + '\n' + sequence)
        return sequences




# Function to divide sequence into words of size 20
def divide_into_words(sequence):
    words = []
    for i in range(0, len(sequence), 20):  # Start from 0, go up to len(sequence), in steps of 20
        word = sequence[i:i + 20]
        words.append(word)
    return words

# Function to compare words and find similar ones
def find_similar_words(word, database):
    similar_words = []
    chunk_size = 70
    output_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\program_output.txt"

    for seq in database:
        if len(seq) >= 20:  # Check if the sequence is long enough
            for j in range(len(seq) - 19):  # Adjust the range to consider the last 20-character segment
                match_count = 0
                for i in range(20):  # Compare 20 characters starting from position j
                    if word[i] == seq[i + j]:
                        match_count += 1
                if match_count >= 12:  # If at least 12 matches are found
                    similar_words.append(seq)  # Append the whole sequence to the list
                    print(f"{word} has {match_count} matches.")
                    with open(output_file_path, 'a') as file:


                        file.write(seq)
                        file.write("\n")
                        file.write("The common sequence in imagination is:   ")
                        file.write(word)
                        file.write("\n")
                        # Add a line to write the matching 20-character segment from 'seq'
                        file.write("Matching segment from database sequence: ")
                        file.write(seq[j:j + 20])  # This writes the specific fragment being compared
                        file.write("\n")
                        file.write("The number of the matches is: ")
                        file.write(str(match_count))
                        file.write("\n")  # Add some new lines for better readability
                        file.write("Position of the matching segment in the database sequence: ")
                        file.write(str(j + 1))  # Position is `j` (0-indexed), so `j+1` gives the 1-indexed position
                        file.write(" - ")
                        file.write(str(j+21))
                        file.write("\n")
                        file.write("\n")
                        file.write("\n")
                    break
    return similar_words

def write_in_chunks(text, file):
    chunk_size = 50
    # Ensure text is a string, join list items if text is a list
    if isinstance(text, list):
        text = ', '.join(text)  # Convert list to string
    for start in range(0, len(text), chunk_size):
        end = start + chunk_size
        file.write(text[start:end] + "\n")
def fork_proteins(input_file_path):
    # Define file paths for output
    tata_box_file_path = input_file_path.replace('.txt', '_TATA_BOX.txt')
    nadp_file_path = input_file_path.replace('.txt', '_NADP.txt')

    try:
        # Open the input file and output files
        with open(input_file_path, 'r') as file, \
             open(tata_box_file_path, 'w') as tata_box_file, \
             open(nadp_file_path, 'w') as nadp_file:

            while True:
                header = file.readline().strip()  # Read the header
                if not header:  # If no more content, break the loop
                    break
                sequence = file.readline().strip()  # Read the sequence

                # Check if the header contains 'TATA-BOX'
                if 'TATA-BOX' in header:
                    tata_box_file.write(f"{header}\n{sequence}\n\n")
                # Check if the header contains 'NADP'
                elif 'NADP' in header:
                    nadp_file.write(f"{header}\n{sequence}\n\n")

    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_path = 'path_to_your_reduced_protein_file.txt'
fork_proteins(input_path)




# Main function
def main():
    # Example sequences
    i = 1
    similar_proteins_count = 1  # Counter for the number of similar proteins
    reduce_count = 2

    sequence2 = "YMYNKITPPTTGEKITFKNGEPVVPDNPIIPFIRGDGTGI"
    sequence1 = "MEYTIKIENVVASTQIGENIDLVKISKEIKDSEYKPKQFP"

    # Database of sequences from a FASTA file
    fasta_file = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\uniFiles"
    all_files = os.listdir(fasta_file)
    txt_files = [file for file in all_files if file.endswith('')]
    output_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\program_output.txt"  # Change this to your desired output file path, e.g.
    for file_name in txt_files:
        file_path = os.path.join(fasta_file, file_name)

        database = read_fasta(file_path)
        print("1")
        print("file path/name :__________________________________________________"
              " ", file_name)
        print("2")
        # Divide sequences into words
        words1 = divide_into_words(sequence1)
        words2 = divide_into_words(sequence2)

        # Find similar words in the database for each sequence
        # Find similar words in the database for each sequence
        similar_words1 = []
        similar_words2 = []
        for word in words1:
            similar_words1 += find_similar_words(word, database)

        for word in words2:
            similar_words2 += find_similar_words(word, database)

        # Print results
        print("Similar words in sequence 1:", similar_words1)
        print("Similar words in sequence 2:", similar_words2)
        similar_proteins_count += 1
    print("Finally we got ", similar_proteins_count, " similar proteins !")



    input_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\program_output.txt"
    output_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\OUTPUT1.txt"

    # Read the first sequence from the file and prepare for comparisons
    try:
        with open(input_file_path, 'r') as file:
            first_header = file.readline().strip()
            first_protein = file.readline().strip()
            if not first_protein:
                raise ValueError("No protein sequences found in the input file.")
    except FileNotFoundError:
        print("The input file does not exist.")
        return
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return

    # Process other sequences and compare them with the first one
    try:
        with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
            # Write the first sequence to the output file before doing comparisons
            output_file.write(f"{first_header}\n{first_protein}\n\n")

            next(file)  # Skip the first header already read
            next(file)  # Skip the first sequence already read
            for header, sequence in zip(file, file):
                header = header.strip()
                sequence = sequence.strip()
                if sequence:
                    # Calculate the number of differences
                    differences = sum(1 for a, b in zip(first_protein, sequence) if a != b)
                    # Adjust for any additional characters in either sequence
                    differences += abs(len(first_protein) - len(sequence))

                    # Write to the output file if differences are more than one
                    if differences > 1:
                        output_file.write(f"{header}\n{sequence}\n\n")

    except FileNotFoundError:
        print("The input file does not exist.")
    except Exception as e:
        print(f"An error occurred while processing sequences: {e}")

        ########################################################################################

    input_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\program_output.txt"
    output_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\OUTPUT2.txt"

    # Read the first sequence from the file and prepare for comparisons
    try:
        with open(input_file_path, 'r') as file:
            first_header = file.readline().strip()
            first_protein = file.readline().strip()
            if not first_protein:
                raise ValueError("No protein sequences found in the input file.")
    except FileNotFoundError:
        print("The input file does not exist.")
        return
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return

    # Process other sequences and compare them with the first one
    try:
        with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
            # Write the first sequence to the output file before doing comparisons
            output_file.write(f"{first_header}\n{first_protein}\n\n")

            next(file)  # Skip the first header already read
            next(file)  # Skip the first sequence already read
            for header, sequence in zip(file, file):
                header = header.strip()
                sequence = sequence.strip()
                if sequence:
                    # Calculate the number of differences
                    differences = sum(1 for a, b in zip(first_protein, sequence) if a != b)
                    # Adjust for any additional characters in either sequence
                    differences += abs(len(first_protein) - len(sequence))

                    # Write to the output file if differences are more than one
                    if differences > 2:
                        output_file.write(f"{header}\n{sequence}\n\n")

    except FileNotFoundError:
        print("The input file does not exist.")
    except Exception as e:
        print(f"An error occurred while processing sequences: {e}")

        ########################################################################################

    input_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\OUTPUT2.txt"
    output_file_path = r"C:\Users\fadi-\PycharmProjects\FinalProject\ProtProject\uniprot_trembl.fasta\Result\OUTPUT3.txt"

    # Read the first sequence from the file and prepare for comparisons with all tests
    try:
        with open(input_file_path, 'r') as file:
            first_header = file.readline().strip()
            first_protein = file.readline().strip()
            if not first_protein:
                raise ValueError("No protein sequences found in the input file.")
    except FileNotFoundError:
        print("The input file does not exist.")
        return
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return

    # Process other sequences and compare them with the first one
    try:
        with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
            # Write the first sequence to the output file before doing comparisons
            output_file.write(f"{first_header}\n{first_protein}\n\n")

            next(file)  # Skip the first header already read
            next(file)  # Skip the first sequence already read
            for header, sequence in zip(file, file):
                header = header.strip()
                sequence = sequence.strip()
                if sequence:
                    # Calculate the number of differences
                    differences = sum(1 for a, b in zip(first_protein, sequence) if a != b)
                    # Adjust for any additional characters in either sequence
                    differences += abs(len(first_protein) - len(sequence))

                    # Write to the output file if differences are more than one
                    if differences > 3:
                        output_file.write(f"{header}\n{sequence}\n\n")


    except FileNotFoundError:
        print("The input file does not exist.")
    except Exception as e:
        print(f"An error occurred while processing sequences: {e}")

    # Simulate processing functions
    def find_similar_proteins():
        # This function would process and return the count of similar proteins
        # Here, we just return a mock number
        return similar_proteins_count

    def count_proteins_after_reduction():
        # This function would process and return the count of proteins after some filtering or reduction
        # Here, we just return a mock number
        return similar_proteins_count / reduce_count

    # Function to update the GUI with results
    def update_counts():
        similar_count = find_similar_proteins()
        reduced_count = count_proteins_after_reduction()
        label_similar.config(text=f"Similar Proteins Found: {similar_count}")
        label_reduced.config(text=f"Proteins After Reduction: {reduced_count}")

    # Create the main window to display number of the similar proteins before and after the reduction
    root = tk.Tk()
    root.title("Protein Analysis")

    # Create a label for showing similar proteins count
    label_similar = tk.Label(root, text="Similar Proteins Found: 0", font=('Helvetica', 16))
    label_similar.pack(pady=10)

    # Create a label for showing proteins count after reduction
    label_reduced = tk.Label(root, text="Proteins After Reduction: 0", font=('Helvetica', 16))
    label_reduced.pack(pady=10)

    # Create a button to update counts
    button_update = tk.Button(root, text="Update Counts", command=update_counts, font=('Helvetica', 16))
    button_update.pack(pady=20)

    # Start the GUI event loop
    root.mainloop()


if __name__ != "__main__":
    pass
else:
    main()
  
