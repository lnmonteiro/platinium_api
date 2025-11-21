import json
from datetime import datetime
import azure.functions as func

def success_response(data, status_code=200):
    """Retorna uma resposta de sucesso padronizada"""
    response = {
        "status": "success",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total": len(data) if isinstance(data, list) else 1,
        "data": data
    }
    
    return func.HttpResponse(
        json.dumps(response, default=str, ensure_ascii=False),
        mimetype="application/json; charset=utf-8",
        status_code=status_code
    )

def error_response(message, details=None, status_code=500):
    """Retorna uma resposta de erro padronizada"""
    response = {
        "status": "error",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "error": {
            "message": message,
            "details": str(details) if details else None
        }
    }
    
    return func.HttpResponse(
        json.dumps(response, ensure_ascii=False),
        mimetype="application/json; charset=utf-8",
        status_code=status_code
    )
    