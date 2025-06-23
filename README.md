# API de Detecção de Phishing

Esta é uma API para detectar se um determinado texto é phishing ou legítimo. O projeto utiliza um modelo de Regressão Logística treinado em um dataset de mensagens de phishing e legítimas.

## Estrutura do Projeto

- `src/`: Contém o código-fonte da aplicação.
  - `main.py`: Ponto de entrada da API FastAPI. Expõe o endpoint `/classify`.
  - `model.py`: Responsável por carregar o dataset, treinar o modelo de machine learning e fornecer a função de classificação.
- `requirements.txt`: Lista as dependências do projeto.

## Como Usar

### Pré-requisitos

- Python 3.8+
- [Conda](https://docs.conda.io/en/latest/miniconda.html) ou um ambiente virtual Python.

### 1. Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/rafabd1/Trabalho-Extensionista
    cd Trabalho-Extensionista
    ```

2.  **Crie e ative o ambiente Conda: (Opicional)**
    ```bash
    conda create --name llm python=3.9
    conda activate llm
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Treinando o Modelo

Antes de iniciar a API, você precisa treinar o modelo e gerar os artefatos. Execute o script de treinamento:

```bash
python src/train.py
```

Este comando irá baixar o dataset, treinar o modelo e salvar os arquivos `vectorizer.joblib` e `model.joblib` em um diretório chamado `artifacts`. Você só precisa fazer isso uma vez.

### 3. Executando a API

1.  Com o modelo treinado, inicie o servidor da API:
    ```bash
    uvicorn src.main:app --reload --port 8080
    ```

2.  Após a inicialização, a API estará disponível em `http://127.0.0.1:8080`.

### 4. Testando o Endpoint

Você pode testar o endpoint de classificação de duas formas:

- **Via Documentação Interativa (Swagger UI):**
  Acesse [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs) no seu navegador para ver a documentação e enviar requisições de teste diretamente pela interface.

- **Via `curl` (ou outra ferramenta de API):**
  Envie uma requisição POST para o endpoint `/classify` com o texto que deseja analisar.

  Exemplo:
  ```bash
  curl -X 'POST' \
    'http://127.0.0.1:8080/classify/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
      "text": "Atenção! Sua conta foi bloqueada. Clique aqui para desbloquear."
    }'
  ```

  **Resposta Esperada:**
  ```json
  {
    "is_phishing": true,
    "confidence": 0.9288972678184793
  }
  ``` 