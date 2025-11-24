import sys
import importlib

# Expected versions from requirements.txt/environment.yml
REQUIRED = {
    "numpy": "1.23.5",
    "pandas": "2.2.0",
    "sklearn": "1.4.0", # scikit-learn imports as `sklearn`
    "xgboost": "1.7.6",
    "lightgbm": "4.3.0",
    "shap": "0.44.1",
    "matplotlib": "3.8.4",
    "seaborn": "0.13.2",
    "joblib": "1.4.0",
    "yaml": "6.0.2",     # pyyaml imports as `yaml`
}

def check(pkg_name, expected_version):
    try:
        module = importlib.import_module(pkg_name)
        installed = getattr(module, "__version__", None)

        if pkg_name == "yaml" or pkg_name == "sklearn":  # PyYAML uses yaml.__version__
            installed = module.__version__

        if installed is None:
            print(f"WARNING: {pkg_name}: could not determine version")
            return False

        if installed == expected_version:
            print(f"OK: {pkg_name} == {installed}")
            return True
        else:
            print(f"ERROR: {pkg_name}: installed {installed}, expected {expected_version}")
            return False

    except ImportError:
        print(f"ERROR: {pkg_name}: not installed")
        return False


def main():
    print("Checking installed versions...\n")

    failures = 0

    for pkg, expected in REQUIRED.items():
        if not check(pkg, expected):
            failures += 1

    print("\nSummary:")
    if failures == 0:
        print("OK: All versions match requirements.txt")
        sys.exit(0)
    else:
        print(f"WARNING: {failures} mismatches found")
        sys.exit(1)


if __name__ == "__main__":
    main()
