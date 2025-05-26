# FuGEP: **Fu**nctional **G**enomics **E**vent **P**rediction Framework

A comprehensive framework for predicting functional genomic events using deep learning approaches.

## 🔗 Multi-Account Repository Access

This repository is synchronized across multiple GitHub accounts for research continuity:

- **Primary**: [SanjeevaRDodlapati/FuGEP](https://github.com/SanjeevaRDodlapati/FuGEP)
- **Mirror 1**: [sdodlapati3/FuGEP](https://github.com/sdodlapati3/FuGEP)  
- **Mirror 2**: [sdodlapa/FuGEP](https://github.com/sdodlapa/FuGEP)

All repositories are kept in perfect synchronization for seamless collaboration.

## ⚡ Quick Start

### Installation

```bash
# Clone from any synchronized repository
git clone git@github.com:SanjeevaRDodlapati/FuGEP.git
# OR: git clone git@github.com:sdodlapati3/FuGEP.git
# OR: git clone git@github.com:sdodlapa/FuGEP.git
cd FuGEP

# Install the package
pip install -e .
```

### 🚀 Multi-Account Development Workflow

#### For Maintainers

```bash
# 1. Develop your functional genomics models
# 2. Commit changes
git add .
git commit -m "Add epigenetic modification prediction model"

# 3. Push to all research accounts instantly
./push_all.csh

# Your research is now backed up across all GitHub accounts!
```

#### For Contributors

```bash
# Fork from any of the synchronized repositories
# Submit pull requests to the primary repository
```

## 🧬 Features

### Functional Genomics Prediction

- **Methylation Analysis**: Predict CpG methylation patterns
- **Chromatin Accessibility**: ATAC-seq and DNase-seq prediction
- **Histone Modifications**: Multi-mark histone modification prediction
- **Gene Expression**: Transcription regulation prediction
- **Variant Effect Analysis**: Functional impact of genetic variants

### Advanced Deep Learning Models

- **DeepCpG Integration**: DNA methylation prediction
- **SEI (Sequence-based Regulatory Element Identifier)**: Regulatory element prediction
- **Custom Architectures**: Specialized models for genomic event prediction

### Configuration-Driven Workflows

FuGEP uses YAML configuration files for reproducible research:

```yaml
# Example: methyl-gve.yml
model_type: "deepcpg"
data_path: "/path/to/methylation/data"
output_dir: "./results/methylation_analysis"
batch_size: 32
learning_rate: 0.001
```

## 🔧 Usage Examples

### DNA Methylation Prediction

```bash
# Train methylation prediction model
python -m fugep train --config methyl-train-h5.yml

# Evaluate methylation patterns
python -m fugep evaluate --config methyl-evaluate-h5.yml
```

### Chromatin Peak Prediction

```bash
# Predict chromatin accessibility peaks
python -m fugep train --config peak-gve-h5.yml
```

### SEI-based Regulatory Analysis

```bash
# Run SEI-based regulatory element prediction
python -m fugep train --config methyl-gve-sei.yml
```

## 🐳 Docker Support

FuGEP includes Docker support for reproducible environments:

```bash
# Build the Docker container
docker build -t fugep .

# Run analysis in container
docker run -v /path/to/data:/data fugep python -m fugep train --config /data/config.yml
```

## 📊 Research Integration

### Multi-Repository Genomic Ecosystem

FuGEP integrates with other genomic deep learning frameworks:

- **GenomicLightning**: PyTorch Lightning-based genomic models
- **UAVarPrior**: Uncertainty-aware variational priors for genomics
- **Multi-account sync**: Seamless collaboration across research platforms

### 🔬 Research Workflow

1. **Data Preparation**: Process genomic datasets using provided scripts
2. **Model Configuration**: Define experiments using YAML configs  
3. **Training**: Execute training with `fugep train`
4. **Analysis**: Interpret results with built-in visualization tools
5. **Publication**: Reproducible research with version-controlled configs

## 🛡️ Quality Assurance

- **Automated Testing**: Continuous integration across all accounts
- **Code Quality**: Automated linting and formatting
- **Security Scanning**: Dependency vulnerability monitoring
- **Documentation**: Synchronized documentation updates

## 🤝 Contributing

### For Research Collaborators

1. Fork from any synchronized repository
2. Create feature branch: `git checkout -b feature-new-prediction-model`
3. Implement your genomic prediction model
4. Add tests and documentation
5. Submit PR to primary repository (SanjeevaRDodlapati/FuGEP)

### Development Standards

- Follow PEP 8 coding standards
- Include comprehensive tests for new models
- Document all configuration parameters
- Ensure reproducibility with fixed random seeds

## 📚 Documentation

- **Configuration Examples**: See `config_examples/` directory
- **Tutorials**: Check `tutorials/` for step-by-step guides
- **API Documentation**: Generated automatically from source code

## 🆘 Support & Troubleshooting

### Common Issues

- **Memory Issues**: Use smaller batch sizes for large genomic datasets
- **CUDA Errors**: Ensure compatible PyTorch and CUDA versions
- **Data Format**: Verify input data follows expected HDF5 structure

### Getting Help

- **Issues**: Report on any synchronized repository
- **Discussions**: Use GitHub Discussions on primary repository
- **Documentation**: Check tutorials and configuration examples

## 📄 License

See LICENSE file for details.

## 🎯 Citation

If you use FuGEP in your research, please cite:

```bibtex
@software{fugep2025,
  title={FuGEP: Functional Genomics Event Prediction Framework},
  author={Your Research Team},
  year={2025},
  url={https://github.com/SanjeevaRDodlapati/FuGEP}
}
```
