# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-11

### Added
- Initial release of Stock Price vs Search Trends Analyzer
- Multi-stock analysis with real-time data
- Integration with Alpha Vantage API for stock prices
- Integration with Google Trends via PyTrends for search interest
- Pearson correlation coefficient calculation
- Dual-axis interactive charts using Plotly
- CSV export functionality
- Mock data mode for development and testing
- Streamlit web UI with intuitive controls
- Stock selection by categories (Technology, Finance, Healthcare, Consumer)
- Custom search keyword support
- Customizable analysis period (30-365 days)
- Comprehensive error handling and fallbacks
- Clean Architecture (Ports & Adapters) pattern
- Dependency injection for flexible configuration
- Complete documentation with usage examples
- Contributing guidelines and community standards

### Infrastructure
- Streamlit web framework
- Pandas for data manipulation
- Plotly for interactive visualizations
- Python 3.12 compatibility
- Virtual environment setup
- MIT License
- Code of Conduct
- Contributing guidelines
- Issue and PR templates

---

## [Unreleased]

### Planned Features
- [ ] Caching layer (Redis/SQLite)
- [ ] Historical correlation tracking
- [ ] Advanced statistics (p-values, confidence intervals)
- [ ] FastAPI backend for programmatic access
- [ ] Machine learning predictions
- [ ] Portfolio analysis
- [ ] Real-time data streaming
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Database persistence

### Improvements
- [ ] Enhanced error messages
- [ ] Performance optimization
- [ ] More comprehensive testing
- [ ] API rate limit optimization
- [ ] User authentication
- [ ] Saved analysis history

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for added backwards-compatible functionality
- **PATCH** version for backwards-compatible bug fixes

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.
