# run_tests.py (place this in your project root directory)
import pytest
import os
import sys
from datetime import datetime

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"Reports/pytest_report_{timestamp}.html"

    # Create directories if they don't exist
    for directory in ["Reports", "Screenshots", "TestData"]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Run pytest with HTML report
    args = [
        "-v",
        "--html=" + report_file,
        "--self-contained-html",
        "./TestCases"  # Use relative path
    ]

    # Add any command-line arguments
    args.extend(sys.argv[1:])

    exit_code = pytest.main(args)

    print(f"Test execution completed. Report saved to {report_file}")
    sys.exit(exit_code)