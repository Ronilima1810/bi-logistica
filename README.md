# Ruby BI · Logistics Intelligence

**Produto demonstrativo de análise logística desenvolvido com React e FastAPI.**

[Live preview — Ruby Logistics Analytics](https://ronilima1810.github.io/formulario-de-matricula/portfolio-demos/ruby/) · [Vitrine de sistemas](https://ronilima1810.github.io/formulario-de-matricula/portfolio-demos/)

> A demonstração utiliza dados 100% sintéticos. A interface pública reproduz o estilo do Ruby; **não é o ambiente corporativo e não se conecta ao banco, WMS ou APIs de produção**.

## Produto

O frontend oferece uma experiência visual de software corporativo, com sidebar, tema claro/escuro, tabelas extensas, indicadores, filtros e exportação CSV. Em vez de apenas cards estáticos, as métricas são recalculadas com base nas seleções de UF e transportadora.

| Visão | Entrega |
| --- | --- |
| Visão executiva | Faturamento, volumetria, frete, percentual total e evolução |
| Eficiência | `Σ fretes / Σ valores NF × 100`, inclusive por transportadora |
| Operação | Distribuição das etapas de faturamento, expedição e entrega |
| Documentos | Detalhamento de pedidos, NF-e, clientes fictícios e valores |
| Performance | Comparativos de parceiros por receita e volume |
| Arquitetura | Explicação dos contratos e limites da demonstração |

## Stack

- **Frontend:** React 19, Vite 7, Lucide, CSS responsivo e componentes funcionais.
- **Backend:** FastAPI + Pydantic com endpoints de demonstração `/api/health`, `/api/shipments` e `/api/metrics`.
- **Persistência:** nenhuma; registros definidos em código, sem credenciais ou banco corporativo.
- **CI:** GitHub Actions valida a compilação frontend e a API.

## Executar frontend

Na pasta `frontend/`:

```bash
npm install
npm run dev
```

Acesse o endereço local informado pelo Vite. Para gerar um build estático: `npm run build`, que escreve em `frontend/dist`.

## Executar API demonstrativa

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Os dados vêm do módulo Python, não de um banco externo. A API demonstrativa e o frontend funcionam independentemente; **integração autenticada entre ambos não foi implementada**.

## Segurança e evolução

Não usar este projeto com dados reais sem criar autenticação, RBAC, validação de entrada, limites de API, logs e conexão segura a fontes autorizadas. Antes de qualquer uso operacional, substituir as fixtures por integrações testadas e revisar os cálculos financeiros contra tabelas contratuais.

**Build verificado:** compilação React/Vite executada com sucesso; dados fictícios e separação da produção preservados.
