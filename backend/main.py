"""API demonstrativa independente, sem banco corporativo e sem credenciais."""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI(title="Ruby BI Demo API",version="1.0.0",docs_url="/api/docs",openapi_url="/api/openapi.json")
class Shipment(BaseModel):
    id: str
    cliente: str
    uf: str
    transportadora: str
    valor_nf: float
    frete: float
    volumes: int
    status: str

DEMO=[
    Shipment(id="DEMO-0140",cliente="Cliente Horizonte",uf="SP",transportadora="Parceiro A",valor_nf=12500,frete=485,volumes=34,status="Entregue"),
    Shipment(id="DEMO-0141",cliente="Varejo Estrela",uf="MG",transportadora="Parceiro B",valor_nf=8760,frete=324,volumes=21,status="Em rota"),
    Shipment(id="DEMO-0142",cliente="Loja Pioneira",uf="PR",transportadora="Parceiro A",valor_nf=17400,frete=710,volumes=48,status="Expedido"),
    Shipment(id="DEMO-0143",cliente="Distribuidora Demo",uf="PE",transportadora="Parceiro C",valor_nf=6590,frete=295,volumes=15,status="Faturado"),
]

@app.get("/api/health")
def health():
    return {"ok":True,"mode":"synthetic","connected_to_production":False}

@app.get("/api/shipments",response_model=list[Shipment])
def shipments(uf:str|None=None):
    return [x for x in DEMO if not uf or x.uf==uf]

@app.get("/api/metrics")
def metrics():
    revenue=sum(x.valor_nf for x in DEMO)
    freight=sum(x.frete for x in DEMO)
    return {"faturamento":revenue,"frete":freight,"volumes":sum(x.volumes for x in DEMO),"frete_percentual":round(100*freight/revenue,2) if revenue else 0,"pedidos":len(DEMO)}
