import azure.functions as func
import logging
from src.shared.database.connection import execute_query
from src.shared.utils.response import success_response, error_response

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    
    if name:
        return success_response({"message": f"Olá, {name}! Bem-vindo à API!"})
    else:
        return success_response({"message": "Olá! Envie um 'name' para te cumprimentar!"})

@app.route(route="products", methods=["GET"])
def get_products(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Getting products from database')
    
    try:
        products = execute_query("EXEC [karen].[GetProducts]")
        
        for product in products:
            if product.get("Tipo de Produto") is None:
                product["Tipo de Produto"] = "Não especificado"
            if product.get("Duração") is None:
                product["Duração"] = 0
        
        return success_response({"produtos": products})
        
    except Exception as e:
        logging.error(f"Error getting products: {str(e)}")
        return error_response("Erro ao buscar produtos", e)