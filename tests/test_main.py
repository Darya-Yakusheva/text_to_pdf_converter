import os
import tempfile
from pathlib import Path

import pytest

from app.main import check_file, convert_file


@pytest.fixture(scope="session")
def temp_dir():
    """
    Fixture to create a temporary directory for testing.
    Cleans up the directory after the test is done.
    """
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temp_dir:
        yield temp_dir  # Provide the directory to the test function


def create_file(directory, filename, content):
    """
    Creates a single file with the given content in the specified directory.
    """
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        file.write(content)
    return filepath


@pytest.mark.parametrize("filename", ["test1.doc", "test2.docx"])
def test_file_creation_and_conversion(temp_dir, filename):
    """
    Test file creation and conversion using parameterized filenames.
    """
    input_file_path = create_file(temp_dir, filename, f"Content of {filename}")
    convert_file(input_file_path, temp_dir)  # converts the file to PDF

    output_file_path = Path(os.path.splitext(input_file_path)[0] + ".pdf")
    assert output_file_path.exists()  # verifies the PDF file was created


test_exceptions_data = [
    # Invalid cases
    (
        "non_supported_file.py",
        ValueError,
        "Unsupported file format .*. Only .doc and .docx are supported.",
    ),
    (
        "non_existent_file.doc",
        FileNotFoundError,
        "Input file .* does not exist."),
]

valid_files_data = [
    # Valid cases
    "file1.doc",
    "file2.DOC",
    "file3.docx",
    "file4.DOCX",
]


@pytest.mark.parametrize(
    "filename,expected_exception,match_message", test_exceptions_data
)
def test_check_file_exceptions(filename, expected_exception, match_message):
    """
    Test that check_file raises the correct exceptions for invalid input.
    """
    with pytest.raises(expected_exception, match=match_message):
        check_file(filename)


@pytest.mark.parametrize("filename", valid_files_data)
def test_check_file_valid_files(filename, mocker):
    """
    Test that check_file does not raise any exceptions for valid files.
    """
    # Mock os.path.exists to simulate the files existing
    mocker.patch("os.path.exists", return_value=True)

    try:
        check_file(filename)
    except Exception as e:
        pytest.fail(f"check_file raised an exception for '{filename}': {e}")
