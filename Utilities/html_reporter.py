
import os
import datetime
from jinja2 import Environment, FileSystemLoader
import time


class HTMLReporter:
    def __init__(self, report_name="Test_Report"):
        self.report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Reports'))
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report_file = os.path.join(self.report_dir, f"{report_name}_{timestamp}.html")

        self.test_results = []
        self.start_time = time.time()

    def add_test_result(self, test_name, status, duration, error_message=None, screenshot=None):
        self.test_results.append({
            "test_name": test_name,
            "status": status,
            "duration": f"{duration:.2f}s",
            "error_message": error_message,
            "screenshot": screenshot
        })

    def generate_report(self):
        end_time = time.time()
        total_duration = end_time - self.start_time

        # Calculate statistics
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["status"] == "PASS")
        failed_tests = total_tests - passed_tests

        pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

        # Create HTML report
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
        template = env.from_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{report_title}}</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #333; }
                .summary { margin: 20px 0; padding: 10px; background-color: #f0f0f0; }
                .test-case { margin: 10px 0; padding: 10px; border: 1px solid #ddd; }
                .pass { background-color: #dff0d8; }
                .fail { background-color: #f2dede; }
                .stats { font-weight: bold; }
                .screenshot { max-width: 800px; margin-top: 10px; }
            </style>
        </head>
        <body>
            <h1>{{report_title}}</h1>
            <div class="summary">
                <p><span class="stats">Total Tests:</span> {{total_tests}}</p>
                <p><span class="stats">Passed:</span> {{passed_tests}} ({{pass_percentage|round(2)}}%)</p>
                <p><span class="stats">Failed:</span> {{failed_tests}}</p>
                <p><span class="stats">Total Duration:</span> {{total_duration|round(2)}}s</p>
                <p><span class="stats">Start Time:</span> {{start_time}}</p>
                <p><span class="stats">End Time:</span> {{end_time}}</p>
            </div>

            <h2>Test Results</h2>
            {% for result in test_results %}
            <div class="test-case {{'pass' if result.status == 'PASS' else 'fail'}}">
                <h3>{{result.test_name}}</h3>
                <p><strong>Status:</strong> {{result.status}}</p>
                <p><strong>Duration:</strong> {{result.duration}}</p>
                {% if result.error_message %}
                <p><strong>Error:</strong> {{result.error_message}}</p>
                {% endif %}
                {% if result.screenshot %}
                <p><strong>Screenshot:</strong></p>
                <img src="{{result.screenshot}}" alt="Screenshot" class="screenshot">
                {% endif %}
            </div>
            {% endfor %}
        </body>
        </html>
        ''')

        html_content = template.render(
            report_title="Test Automation Report",
            total_tests=total_tests,
            passed_tests=passed_tests,
            failed_tests=failed_tests,
            pass_percentage=pass_percentage,
            total_duration=total_duration,
            start_time=datetime.datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S'),
            end_time=datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S'),
            test_results=self.test_results
        )

        with open(self.report_file, 'w') as f:
            f.write(html_content)

        return self.report_file