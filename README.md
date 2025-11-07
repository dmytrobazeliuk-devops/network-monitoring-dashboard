# Network Monitoring Dashboard

Real-time network monitoring dashboard with custom visualizations monitoring 50+ network devices. Features automated alerting and historical data analysis.

## Features

- **Real-time Monitoring**: Live network statistics
- **System Metrics**: CPU, memory, and disk usage
- **Health Checks**: Port and connectivity monitoring
- **REST API**: JSON API for integration
- **Web Dashboard**: Interactive web interface

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run dashboard

```bash
python dashboard.py
```

Access the dashboard at http://localhost:5000

## API Endpoints

- `GET /api/network` - Network statistics
- `GET /api/system` - System information
- `GET /api/health` - Health check status

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

**Dmytro Bazeliuk**
- Portfolio: https://devsecops.cv
- GitHub: [@dmytrobazeliuk-devops](https://github.com/dmytrobazeliuk-devops)
