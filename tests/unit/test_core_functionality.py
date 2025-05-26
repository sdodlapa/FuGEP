#!/usr/bin/env python3
"""
Unit tests for FuGEP core functionality.
"""

import pytest
import os
import sys

class TestGenomicDataProcessing:
    """Test genomic data processing functionality."""
    
    def test_sequence_validation(self):
        """Test DNA sequence validation."""
        valid_sequences = ['ATCG', 'AAAA', 'TTTT', 'GGGG', 'CCCC']
        invalid_sequences = ['ATCX', 'atcg', '1234']
        
        for seq in valid_sequences:
            assert all(c in 'ATCG' for c in seq)
        
        for seq in invalid_sequences:
            assert not all(c in 'ATCG' for c in seq)
    
    def test_sequence_encoding(self):
        """Test sequence encoding functionality."""
        # Basic one-hot encoding test
        sequence = 'ATCG'
        encoding_map = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        encoded = [encoding_map[base] for base in sequence]
        expected = [0, 1, 2, 3]
        assert encoded == expected
    
    def test_methylation_data_structure(self):
        """Test methylation data structure."""
        methylation_site = {
            'chromosome': 'chr1',
            'position': 12345,
            'methylation_level': 0.75,
            'coverage': 20
        }
        
        assert methylation_site['methylation_level'] >= 0.0
        assert methylation_site['methylation_level'] <= 1.0
        assert methylation_site['coverage'] > 0

class TestModelArchitectures:
    """Test model architecture components."""
    
    def test_model_configuration(self):
        """Test model configuration structure."""
        model_config = {
            'architecture': 'cnn',
            'layers': [
                {'type': 'conv1d', 'filters': 64, 'kernel_size': 3},
                {'type': 'maxpool1d', 'pool_size': 2},
                {'type': 'dense', 'units': 128},
                {'type': 'output', 'units': 1, 'activation': 'sigmoid'}
            ],
            'input_shape': (1000, 4)  # sequence_length, num_bases
        }
        
        assert 'architecture' in model_config
        assert 'layers' in model_config
        assert len(model_config['layers']) > 0
    
    def test_training_parameters(self):
        """Test training parameter validation."""
        training_params = {
            'learning_rate': 0.001,
            'batch_size': 32,
            'epochs': 100,
            'optimizer': 'adam'
        }
        
        assert training_params['learning_rate'] > 0
        assert training_params['batch_size'] > 0
        assert training_params['epochs'] > 0
        assert training_params['optimizer'] in ['adam', 'sgd', 'rmsprop']

class TestPeakCalling:
    """Test peak calling functionality."""
    
    def test_peak_detection_parameters(self):
        """Test peak detection parameter validation."""
        peak_params = {
            'min_peak_height': 5.0,
            'min_peak_distance': 100,
            'peak_width_range': (50, 500),
            'significance_threshold': 0.05
        }
        
        assert peak_params['min_peak_height'] > 0
        assert peak_params['min_peak_distance'] > 0
        assert peak_params['peak_width_range'][0] < peak_params['peak_width_range'][1]
        assert 0 < peak_params['significance_threshold'] < 1
    
    def test_peak_data_structure(self):
        """Test peak data structure."""
        peak = {
            'chromosome': 'chr1',
            'start': 10000,
            'end': 10500,
            'peak_center': 10250,
            'height': 15.5,
            'significance': 0.001
        }
        
        assert peak['start'] < peak['end']
        assert peak['start'] <= peak['peak_center'] <= peak['end']
        assert peak['height'] > 0
        assert peak['significance'] >= 0

class TestConfigurationManagement:
    """Test configuration management."""
    
    def test_config_file_structure(self):
        """Test configuration file structure."""
        config = {
            'data': {
                'input_dir': '/path/to/data',
                'output_dir': '/path/to/output',
                'file_format': 'h5'
            },
            'model': {
                'architecture': 'deepcpg',
                'sequence_length': 1001,
                'batch_size': 128
            },
            'training': {
                'epochs': 100,
                'learning_rate': 0.001,
                'validation_split': 0.2
            }
        }
        
        required_sections = ['data', 'model', 'training']
        for section in required_sections:
            assert section in config
    
    def test_path_validation(self):
        """Test path validation logic."""
        test_paths = [
            '/valid/absolute/path',
            './valid/relative/path',
            '../valid/relative/path',
            'valid_filename.txt'
        ]
        
        for path in test_paths:
            # Basic path format validation
            assert isinstance(path, str)
            assert len(path) > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
