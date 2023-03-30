import subprocess

def run_tests():
    generate_backend_reports = f"behave -f behave_html_formatter:HTMLFormatter -o reports/backend/report_backend.html  backend/features/"
    subprocess.call(generate_backend_reports, shell=True)
    generate_frontend_reports = f"behave -f behave_html_formatter:HTMLFormatter -o reports/frontend/report_frontend.html  frontend/features/feature_files/"
    subprocess.call(generate_frontend_reports, shell=True)

if __name__ == '__main__':
    run_tests()