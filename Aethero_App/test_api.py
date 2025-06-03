import pytest
import httpx
from fastapi.testclient import TestClient
import sys
import os

# Add current directory to path to import syntaxator_fastapi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from syntaxator_fastapi import app

# Create test client
client = TestClient(app)

class TestAetheroAPI:
    """Unit tests for Aethero Cognitive Flow API"""
    
    def test_root_endpoint(self):
        """Test the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Welcome to AetheroOS Syntaxator API!"
        assert data["version"] == "1.0.0"
    
    def test_health_endpoint(self):
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["version"] == "1.0.0"
        assert data["service"] == "Aethero Cognitive Flow API"
        assert "timestamp" in data
    
    def test_logs_endpoint(self):
        """Test the logs endpoint"""
        response = client.get("/logs")
        assert response.status_code == 200
        data = response.json()
        assert "logs" in data
        assert "timestamp" in data
    
    def test_parse_endpoint_success(self):
        """Test the parse endpoint with valid ASL text"""
        test_data = {
            "text": "[@cognitive_load:7 @certainty:0.85 @mental_state:focused @emotion:analytical] Test ASL parsing."
        }
        response = client.post("/parse", json=test_data)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "parsed_data" in data
        assert "session_id" in data["parsed_data"]
    
    def test_parse_endpoint_invalid_input(self):
        """Test the parse endpoint with invalid input"""
        test_data = {
            "text": ""
        }
        response = client.post("/parse", json=test_data)
        assert response.status_code == 200  # Should still work with empty string
        data = response.json()
        assert data["status"] == "success"
    
    def test_parse_endpoint_missing_text(self):
        """Test the parse endpoint with missing text field"""
        response = client.post("/parse", json={})
        assert response.status_code == 422  # Validation error
    
    def test_metrics_endpoint_success(self):
        """Test the metrics endpoint with valid data"""
        test_data = {
            "data": "[@cognitive_load:7 @certainty:0.85 @mental_state:focused @emotion:analytical] Test metrics analysis."
        }
        response = client.post("/metrics", json=test_data)
        assert response.status_code == 200
        data = response.json()
        assert "analysis_report" in data
        assert data["status"] in ["success", "basic_analysis"]
    
    def test_metrics_endpoint_empty_data(self):
        """Test the metrics endpoint with empty data"""
        test_data = {
            "data": ""
        }
        response = client.post("/metrics", json=test_data)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "basic_analysis"
        assert "basic_analysis" in data["analysis_report"]
    
    def test_reflect_endpoint_success(self):
        """Test the reflect endpoint with valid input"""
        test_data = {
            "text": "[@cognitive_load:7 @certainty:0.85 @mental_state:focused @emotion:analytical] Reflecting on cognitive patterns.",
            "context": "test_analysis"
        }
        response = client.post("/reflect", json=test_data)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "reflection_result" in data
        assert data["context"] == "test_analysis"
        assert "timestamp" in data
    
    def test_reflect_endpoint_default_context(self):
        """Test the reflect endpoint with default context"""
        test_data = {
            "text": "Simple reflection test."
        }
        response = client.post("/reflect", json=test_data)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["context"] == "general"  # Default value
    
    def test_invalid_endpoint(self):
        """Test accessing non-existent endpoint"""
        response = client.get("/nonexistent")
        assert response.status_code == 404
    
    def test_method_not_allowed(self):
        """Test using wrong HTTP method"""
        response = client.get("/parse")  # Should be POST
        assert response.status_code == 405

# Integration tests
class TestAetheroAPIIntegration:
    """Integration tests for complex workflows"""
    
    def test_parse_then_metrics_workflow(self):
        """Test parsing followed by metrics analysis"""
        # First parse some ASL text
        parse_data = {
            "text": "[@cognitive_load:8 @certainty:0.9 @mental_state:contemplative @emotion:empathetic] Deep cognitive analysis test."
        }
        parse_response = client.post("/parse", json=parse_data)
        assert parse_response.status_code == 200
        
        # Then analyze metrics on the same text
        metrics_data = {
            "data": parse_data["text"]
        }
        metrics_response = client.post("/metrics", json=metrics_data)
        assert metrics_response.status_code == 200
        
        # Both should succeed
        parse_result = parse_response.json()
        metrics_result = metrics_response.json()
        assert parse_result["status"] == "success"
        assert metrics_result["status"] in ["success", "basic_analysis"]
    
    def test_full_cognitive_pipeline(self):
        """Test complete cognitive processing pipeline"""
        test_text = "[@cognitive_load:9 @certainty:0.95 @mental_state:focused @emotion:analytical] Advanced cognitive processing test for full pipeline validation."
        
        # 1. Parse the text
        parse_response = client.post("/parse", json={"text": test_text})
        assert parse_response.status_code == 200
        
        # 2. Analyze metrics
        metrics_response = client.post("/metrics", json={"data": test_text})
        assert metrics_response.status_code == 200
        
        # 3. Perform reflection
        reflect_response = client.post("/reflect", json={
            "text": test_text,
            "context": "pipeline_test"
        })
        assert reflect_response.status_code == 200
        
        # All should succeed
        parse_result = parse_response.json()
        metrics_result = metrics_response.json()
        reflect_result = reflect_response.json()
        
        assert parse_result["status"] == "success"
        assert metrics_result["status"] in ["success", "basic_analysis"]
        assert reflect_result["status"] == "success"
        assert reflect_result["context"] == "pipeline_test"

if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
