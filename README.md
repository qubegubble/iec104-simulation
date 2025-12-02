# IEC104 Simulation

This repository provides a lightweight simulator for an IEC 60870-5-104 (IEC 104) capable device. It can be used to emulate datapoints, respond to interrogations, and transmit spontaneous data using the `c104` Python bindings. The simulator is useful for integration testing, development of SCADA components, and experimenting with IEC 104 behaviour.

**Features**
- **Datapoint model**: Loads point metadata from `Datapoints.json` and creates simulated points.
- **Value simulation**: Provides deterministic and randomized helpers in `src/data_simulator.py` (voltage, frequency, current, power).
- **Server & client examples**: Example server in `src/batch_server.py` and a client example in `src/client.py`.
- **Tests**: Basic pytest test-suite under `tests/` which exercises core utilities.
- **Docker support**: `Dockerfile` and `Dockerfile.alpine` are included to build container images for CI and runtime.

**Quick Start (Windows PowerShell)**

- Prerequisites: `python` (3.11+ recommended), `git`, optional: `docker` / Docker Desktop.
- Create and activate a virtual environment from the project root:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\.venv\Scripts\Activate.ps1
```

- Install project dependencies (this installs `c104` and `pytest` as listed in `requirements.txt`):

```powershell
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt
```

- Run tests locally:

```powershell
python -m pytest -q
```

**Run the simulator locally**

- The repository includes example scripts. To start the batch server (requires `c104` working on your system):

```powershell
python src\batch_server.py
```

- To run the client example (connects to `127.0.0.1:2404` by default):

```powershell
python src\client.py
```

Inspect `Datapoints.json` to see the datapoint metadata the server will load.

**Using Docker (optional)**

- Build the image locally (if Docker Desktop / engine is available):
```powershell
docker build -t iec104-simulation:local -f Dockerfile .
```

- Run tests inside the image (image must include test deps and sources copied in the Dockerfile):
```powershell
docker run --rm iec104-simulation:local python -m pytest -q
```

If you cannot run Docker locally, this repository includes a GitHub Actions workflow at `.github/workflows/ci.yml` that builds the container and runs tests in CI.

**CI / GitHub Actions**

- The example workflow builds the Docker image in the runner and runs tests inside it. It uses `docker/build-push-action` with `load: true` so the built image is available to run in the same job.
- If you want to publish images, adjust the workflow to push to GHCR and provide appropriate secrets/permissions.

**Notes & Troubleshooting**

- The simulator depends on the `c104` package (a Python binding for IEC 104 functionality). If `pip install -r requirements.txt` fails, ensure your environment meets any platform-specific prerequisites required by `c104`.
- If `docker` reports errors like "open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified", Docker Desktop or the Docker engine is not running — start Docker Desktop or use CI instead.
- If you have branch-name mismatches with CI (for example your repo uses `master` or `main`), update `.github/workflows/ci.yml` triggers to match your default branch.

**Contributing**

- Bug reports and PRs are welcome. Please add tests for new features and follow the simple style used in the codebase.

**License**

- Add a `LICENSE` file to this repo to document the intended license (MIT is a common choice). If none exists, the project is currently unlicensed.

**Contact**

- Questions or suggestions: open an issue in this repository.
# iec104-simulation
Small Python project that can simulate a IEC 60870-5-104 capable device.
