"""Tests for NexusProbe attack surface mapper."""

import pytest
import asyncio
from shadow313.tools.nexusprobe import NexusProbe
from shadow313.tools.base import ToolResult


class TestNexusProbe:
    """Test suite for NexusProbe."""

    def test_init(self):
        """Test NexusProbe initialization."""
        probe = NexusProbe()
        assert probe.TOOL_NAME == "nexusprobe"
        assert probe.TEAM == "redteam"

    @pytest.mark.asyncio
    async def test_basic_probe(self):
        """Test basic probe functionality."""
        probe = NexusProbe()
        result = await probe.run("example.com")

        assert isinstance(result, ToolResult)
        assert result.target == "example.com"
        assert result.tool_name == "nexusprobe"
        assert result.success is True
        assert len(result.data) > 0

    @pytest.mark.asyncio
    async def test_with_recon_data(self):
        """Test with provided recon data."""
        probe = NexusProbe()
        recon_data = {
            "target": "test.com",
            "ports": [
                {"port": 22, "state": "open", "service": "ssh", "banner": "OpenSSH 8.9"},
                {"port": 80, "state": "open", "service": "http", "banner": "nginx/1.18"},
            ],
            "web": {"status_code": 200, "technologies": ["nginx"], "https": False},
            "subdomains": [],
        }

        result = await probe.run("test.com", recon_data=recon_data)

        assert result.success is True
        assert result.data["target"] == "test.com"
        assert result.data["total_nodes"] > 0
        assert "scored_nodes" in result.data
        assert "attack_graph" in result.data

    def test_score_to_severity(self):
        """Test severity scoring."""
        probe = NexusProbe()

        assert probe._score_to_severity(9.5) == "CRITICAL"
        assert probe._score_to_severity(7.5) == "HIGH"
        assert probe._score_to_severity(5.5) == "MEDIUM"
        assert probe._score_to_severity(3.0) == "LOW"

    def test_map_to_mitre(self):
        """Test MITRE ATT&CK mapping."""
        probe = NexusProbe()

        assert probe._map_to_mitre("ssh") == "T1021.004"
        assert probe._map_to_mitre("http") == "T1190"
        assert probe._map_to_mitre("unknown") == "T1046"

    def test_build_attack_nodes(self):
        """Test attack node building."""
        probe = NexusProbe()
        recon_data = {
            "ports": [
                {"port": 22, "state": "open", "service": "ssh", "banner": "OpenSSH"},
                {"port": 80, "state": "closed", "service": "http", "banner": ""},
            ],
            "web": {"status_code": 200, "technologies": ["nginx"], "https": True},
            "subdomains": ["api.example.com"],
        }

        nodes = probe._build_attack_nodes("example.com", recon_data)

        # Should have: 1 open port + 1 web tech + 1 subdomain = 3 nodes
        assert len(nodes) == 3
        assert nodes[0]["service"] == "ssh"
        assert nodes[1]["service"] == "nginx"
        assert nodes[2]["host"] == "api.example.com"

    def test_calculate_surface_score(self):
        """Test surface score calculation."""
        probe = NexusProbe()
        nodes = [
            {"attack_score": 9.0},
            {"attack_score": 7.0},
            {"attack_score": 5.0},
        ]

        score = probe._calculate_total_surface_score(nodes)
        assert 0.0 <= score <= 10.0
        assert score > 0.0

    @pytest.mark.asyncio
    async def test_ai_context(self):
        """Test AI context generation."""
        probe = NexusProbe()
        result = await probe.run("example.com")

        context = probe.ai_context(result)

        assert "example.com" in context
        assert "Attack Nodes" in context
        assert "Surface Score" in context
