import os
import subprocess

SUPPORTED_EXTENSIONS = {".doc", ".docx"}


def check_file(input_file):
    """
    Validates the input file for existence and supported extension.

    Args:
        input_file (str): Path to the input file to validate.

    Raises:
        ValueError: If the file's extension is not supported (.doc, .docx).
        FileNotFoundError: If the input file does not exist.
    """
    # Extract the file extension from the input file's name
    _, extension = os.path.splitext(input_file)

    # Check if the file extension is in the list of supported formats
    # (case-insensitive to allow both uppercase and lowercase extensions)
    if extension.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file format {extension}. "
            f"Only .doc and .docx are supported."
        )

    # Check if the file exists on the filesystem
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist.")


def convert_file(input_file, output_dir=None):
    """
    Converts a .doc or .docx file to PDF using LibreOffice.

    Args:
        input_file (str): Path to the input file. Must be a .doc or .docx file.
        output_dir (str, optional): Directory where the PDF will be saved.
                                    If not provided, the PDF will be saved
                                    in the same directory as the input file.

    Returns:
        str: Path to the directory where the converted PDF is saved.

    Raises:
        ValueError: If the file extension is unsupported.
        FileNotFoundError: If the input file does not exist.
    """
    # Validate the input file's existence and format
    check_file(input_file)

    # Default output directory to the input file's directory if not specified
    output_dir = output_dir or os.path.dirname(input_file)

    # Run the LibreOffice command to convert the file to PDF
    # - '--headless' runs LibreOffice in background mode
    # - '--convert-to pdf' specifies the output format
    # - '--outdir' sets the output directory
    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            input_file,
            "--outdir",
            output_dir,
        ],
        check=True,
    )

    # Return the path to the directory where the PDF is saved
    return output_dir


if __name__ == "__main__":
    """
    Entry point of the script:
    - Prompts the user for a file path to convert.
    - Converts the specified file to a PDF using the `convert_file` function.
    - Displays the output directory of the converted PDF.
    """

    # Prompt the user to enter the path to the file they want to convert
    input_file = input("link to file: ")

    # Call the convert_file function to perform the conversion
    # This function will validate the file, handle conversion,
    # and return the output directory
    out_dir = convert_file(input_file)

    # Inform the user that the conversion was successful
    # and display the output directory
    print(f"File successfully converted to PDF in: {out_dir}")
