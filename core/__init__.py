"""
Core module for the Neural Flow Engine.
Exposes the Directed Acyclic Graph (DAG) compiler and the Vector Knowledge Base.
"""

from .flow_parser import NeuralFlow
from .knowledge_base import VectorKnowledgeBase

__all__ = ["NeuralFlow", "VectorKnowledgeBase"]