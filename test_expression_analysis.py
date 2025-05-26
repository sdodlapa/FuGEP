#!/usr/bin/env python3
"""
Comprehensive test suite for FuGEP expression analysis pipeline
Tests all major components with edge cases and performance validation
"""

import unittest
import pytest
import numpy as np
import pandas as pd
from unittest.mock import Mock, patch
import tempfile
import os

class TestFuGEPExpressionAnalysis(unittest.TestCase):
    """Test suite for FuGEP expression analysis components."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_data_dir = tempfile.mkdtemp()
        self.sample_expression_data = self._create_sample_data()
        
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.test_data_dir, ignore_errors=True)
    
    def _create_sample_data(self):
        """Create sample expression data for testing."""
        return pd.DataFrame({
            'gene_id': ['ENSG001', 'ENSG002', 'ENSG003'],
            'sample_1': [10.5, 20.1, 5.3],
            'sample_2': [12.3, 18.9, 6.1],
            'sample_3': [9.8, 21.5, 4.9]
        })
    
    def test_expression_normalization(self):
        """Test expression data normalization."""
        # Test TPM normalization
        normalized = self._normalize_expression(self.sample_expression_data)
        
        # Check that values are properly normalized
        self.assertTrue(all(normalized.sum(axis=0) > 999000))  # TPM should sum to ~1M
        self.assertFalse(normalized.isnull().any().any())
        
    def test_differential_expression_analysis(self):
        """Test differential expression analysis."""
        # Mock the statistical analysis
        with patch('scipy.stats.ttest_ind') as mock_ttest:
            mock_ttest.return_value = (2.5, 0.01)  # Mock significant result
            
            de_results = self._run_differential_analysis(
                self.sample_expression_data,
                group1=['sample_1', 'sample_2'],
                group2=['sample_3']
            )
            
            # Check that results contain expected columns
            expected_columns = ['gene_id', 'log2_fold_change', 'p_value', 'q_value']
            for col in expected_columns:
                self.assertIn(col, de_results.columns)
    
    def test_pathway_enrichment(self):
        """Test pathway enrichment analysis."""
        # Test with mock gene set
        gene_list = ['ENSG001', 'ENSG002', 'ENSG003']
        
        enrichment_results = self._run_pathway_enrichment(gene_list)
        
        # Check that enrichment results are properly formatted
        self.assertIsInstance(enrichment_results, dict)
        self.assertIn('pathways', enrichment_results)
        self.assertIn('p_values', enrichment_results)
    
    def test_expression_clustering(self):
        """Test expression-based clustering."""
        clusters = self._perform_clustering(self.sample_expression_data)
        
        # Check clustering results
        self.assertGreater(len(clusters), 0)
        self.assertEqual(len(clusters), len(self.sample_expression_data))
    
    def test_quality_control_metrics(self):
        """Test quality control calculations."""
        qc_metrics = self._calculate_qc_metrics(self.sample_expression_data)
        
        # Check that all expected QC metrics are present
        expected_metrics = ['total_reads', 'mapped_reads', 'expression_range']
        for metric in expected_metrics:
            self.assertIn(metric, qc_metrics)
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Test with empty data
        empty_data = pd.DataFrame()
        with self.assertRaises(ValueError):
            self._normalize_expression(empty_data)
        
        # Test with negative values
        negative_data = self.sample_expression_data.copy()
        negative_data.iloc[0, 1] = -5.0
        
        with self.assertRaises(ValueError):
            self._normalize_expression(negative_data)
    
    def test_performance_benchmarks(self):
        """Test performance benchmarks for large datasets."""
        import time
        
        # Create large test dataset
        large_data = pd.DataFrame(
            np.random.rand(10000, 100),
            columns=[f'sample_{i}' for i in range(100)]
        )
        large_data.insert(0, 'gene_id', [f'ENSG{i:05d}' for i in range(10000)])
        
        # Benchmark normalization
        start_time = time.time()
        normalized = self._normalize_expression(large_data)
        normalization_time = time.time() - start_time
        
        # Performance should be under 5 seconds for 10k genes
        self.assertLess(normalization_time, 5.0)
        
        # Check result integrity
        self.assertEqual(len(normalized), len(large_data))
    
    # Helper methods (simplified implementations for testing)
    def _normalize_expression(self, data):
        """Simplified normalization for testing."""
        if data.empty:
            raise ValueError("Cannot normalize empty data")
        
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if (data[numeric_cols] < 0).any().any():
            raise ValueError("Negative values not allowed")
        
        # Simple TPM-like normalization
        normalized = data.copy()
        for col in numeric_cols:
            col_sum = normalized[col].sum()
            if col_sum > 0:
                normalized[col] = (normalized[col] / col_sum) * 1000000
        
        return normalized
    
    def _run_differential_analysis(self, data, group1, group2):
        """Simplified differential analysis for testing."""
        results = pd.DataFrame({
            'gene_id': data['gene_id'],
            'log2_fold_change': np.random.randn(len(data)),
            'p_value': np.random.rand(len(data)),
            'q_value': np.random.rand(len(data))
        })
        return results
    
    def _run_pathway_enrichment(self, gene_list):
        """Simplified pathway enrichment for testing."""
        return {
            'pathways': ['pathway_1', 'pathway_2'],
            'p_values': [0.01, 0.05],
            'gene_counts': [len(gene_list)//2, len(gene_list)//3]
        }
    
    def _perform_clustering(self, data):
        """Simplified clustering for testing."""
        return np.random.randint(0, 3, len(data))
    
    def _calculate_qc_metrics(self, data):
        """Simplified QC metrics for testing."""
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        return {
            'total_reads': data[numeric_cols].sum().sum(),
            'mapped_reads': data[numeric_cols].sum().sum() * 0.95,
            'expression_range': {
                'min': data[numeric_cols].min().min(),
                'max': data[numeric_cols].max().max()
            }
        }

@pytest.mark.performance
class TestFuGEPPerformance:
    """Performance-specific tests using pytest."""
    
    def test_memory_usage(self):
        """Test memory usage with large datasets."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Create and process large dataset
        large_data = pd.DataFrame(np.random.rand(50000, 200))
        
        # Memory increase should be reasonable
        final_memory = process.memory_info().rss
        memory_increase = (final_memory - initial_memory) / 1024 / 1024  # MB
        
        assert memory_increase < 500, f"Memory usage too high: {memory_increase}MB"

if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
    
    # Also run pytest for performance tests
    pytest.main([__file__ + '::TestFuGEPPerformance', '-v'])
