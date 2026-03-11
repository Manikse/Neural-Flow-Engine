import sys
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Ensure the core module is accessible within the execution path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.flow_parser import NeuralFlow

router = APIRouter()
engine = NeuralFlow()

class TaskPayload(BaseModel):
    task_description: str

class ExecutionResponse(BaseModel):
    status: str
    nodes_compiled: int
    execution_matrix: list[dict]

@router.post("/compile-and-execute", response_model=ExecutionResponse)
async def process_task(payload: TaskPayload):
    """
    Ingests natural language parameters, compiles the deterministic DAG via the Neural Flow Engine, 
    and returns the execution matrix.
    """
    try:
        # Step 1: Compile the Directed Acyclic Graph (DAG) based on the input vector
        compiled_nodes = engine.compile_dag(payload.task_description)
        
        # Step 2: Traverse the DAG and execute deterministic operations
        engine.execute()
        
        # Step 3: Return the structured execution data to the frontend
        return ExecutionResponse(
            status="execution_successful",
            nodes_compiled=len(compiled_nodes),
            execution_matrix=compiled_nodes
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Fatal error during DAG compilation or execution: {str(e)}"
        )