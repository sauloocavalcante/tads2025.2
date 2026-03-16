# 📈 Stocks History Dashboard

Uma aplicação web interativa para visualização de séries históricas de preços de ações, criptomoedas e ETFs, construída com Python, Streamlit e Plotly.

---

## 🖥️ Demonstração

Insira qualquer ticker no campo lateral (ex: `AAPL`, `TSLA`, `BTC-USD`) e o gráfico de preço de fechamento histórico é gerado automaticamente.

---

## 🚀 Funcionalidades

- Busca de qualquer ativo financeiro via ticker (ações, criptomoedas, ETFs)
- Download automático de dados históricos via Yahoo Finance
- Gráfico interativo de preço de fechamento ao longo do tempo
- Interface simples com sidebar para troca de ticker em tempo real

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| [Python](https://www.python.org/) | Linguagem principal |
| [Streamlit](https://streamlit.io/) | Interface web |
| [Plotly](https://plotly.com/) | Gráficos interativos |
| [yfinance](https://github.com/ranaroussi/yfinance) | Dados do Yahoo Finance |
| [Pandas](https://pandas.pydata.org/) | Manipulação de dados |

---

## 📁 Estrutura do Projeto

```
stocks-dashboard/
│
├── app.py                  # Aplicação principal (Streamlit)
├── requirements.txt        # Dependências do projeto
│
└── functions/
    ├── download.py         # Download de dados via yfinance
    └── plot.py             # Geração do gráfico com Plotly
```

---

## ⚙️ Como executar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/sauloocavalcante/stocks-dashboard.git
cd stocks-dashboard
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute a aplicação**
```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`.

---

## 📦 Principais dependências

```
streamlit==1.53.1
plotly==6.5.2
yfinance==1.0
pandas==2.3.3
```

---

## 👤 Autor

**Saulo Cavalcante**  
[LinkedIn](https://linkedin.com/in/sauloocavalcante) • [GitHub](https://github.com/sauloocavalcante)
