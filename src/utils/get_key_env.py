import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def get_api_key(catalog: str = "secrets_catalog", schema: str = "secrets", key: str = "football-api-analytics") -> str:
    """
    Tenta buscar a chave de API do Unity Catalog Secrets (Databricks) 
    ou faz o fallback para o arquivo .env localmente.
    """
    try:
        import IPython
        dbutils = IPython.get_ipython().user_ns.get("dbutils")
        
        if dbutils:
            uc_catalog = catalog or "workspace"
            uc_schema = schema or "default"
            uc_key = key or "football-api-analytics"
            
            return dbutils.secrets.get(catalog=uc_catalog, schema=uc_schema, key=uc_key)
    except Exception as e:
        if "dbutils" in locals() and dbutils:
            raise RuntimeError(f"Erro ao acessar os segredos do Unity Catalog: {e}")

    # 2. Fallback para ambiente local (.env)
    # api_key_local = os.getenv("FOOTBALL_API_ANALYTICS")
    api_key_local = os.getenv("FOOTBALL_API_STRUCTURAL")
    if api_key_local:
        return api_key_local

    # 3. Se nada funcionar, estoura o erro explicativo
    raise ValueError(
        "Chave da API não encontrada! Certifique-se de configurar o .env localmente "
        "ou executar dentro do Databricks com o Secret Scope configurado."
    )