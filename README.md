# Neural Flow Engine (NFE)

Neural Flow Engine (NFE) is an Engine-as-a-Code framework designed to isolate non-deterministic LLM operations from strict mathematical execution. NFE parses natural language into a directed acyclic graph (DAG) of executable Python nodes, grounding operations in verified engineering standards via Retrieval-Augmented Generation (RAG). 

AI orchestrates the pipeline; Python executes the mathematics.

## Key Features
* Deterministic Node Compilation: Translates natural language intent into a sequence of strict, hardcoded functional nodes.
* RAG-Powered Compliance Constraints: Injects context from local vector databases containing ISO/DIN standards prior to mathematical execution.
* Zero Hallucination Architecture: Numerical models and logical operations are processed exclusively by the Python backend, ensuring absolute precision.
* Dynamic Pipeline Routing: Automatically constructs and connects required operational nodes based on the analyzed complexity of the input task.

## Tech Stack
* Core Logic: Python 3.10+
* Data Retrieval: Local Vector Database mapping / RAG architecture
* Orchestration: LLM-driven natural language parsing to JSON parameters

## Project Structure
* `core/flow_parser.py`: The central processor. Interprets intent, queries standards, and constructs the execution DAG.
* `core/knowledge_base.py`: The interface for querying local engineering constraints and documentation.

## Future Roadmap
[ ] Full injection of autonomous operational agents.
[ ] Implementation of a visual node-based builder within the VestaStack environment.
[ ] Real-time PDF parsing algorithms for automated technical data extraction.

## Author
manikse

Student at Slovak University of Technology (STU), Bratislava
Founder of VestaStack & Lume
Specializing in Automation and Informatization of Processes

<p align="center">
<a href="https://ko-fi.com/manikse">
<img src="https://storage.ko-fi.com/cdn/kofi3.png?v=3" alt="Support the developer at ko-fi.com" width="200">
</a>

<em>If NFE is accelerating your automation capabilities, consider supporting the developer.</em>
</p>

<p align="center">
Engineered by manikse
</p>
.
