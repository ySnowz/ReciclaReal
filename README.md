# Sistema de Gestão de Reciclagem com Streamlit <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Recycling%20Symbol.png" alt="Recycling Symbol" width="25" height="25" />

Este é um sistema completo para gestão de materiais recicláveis, desenvolvido em Python com **Streamlit**, **Pandas** e **CSV**. Permite registrar entradas de materiais, gerar relatórios periódicos e analisar estatísticas de reciclagem.

## Funcionalidades <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Sparkles.png" alt="Sparkles" width="25" height="25" />

- **Registro de Materiais:** Cadastro de entradas com tipo, peso (kg) e valor por kg
- **Relatórios Automáticos:** Geração de CSVs diários e mensais
- **Dashboard Interativo:** Visualização de estatísticas e tendências
  - Materiais mais reciclados
  - Valor total gerado
  - Média diária por material
  - Gráficos comparativos

## Tecnologias Utilizadas <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" alt="Gear" width="25" height="25" />

- **Streamlit** para interface web responsiva
- **Pandas** para processamento de dados
- **CSV** para armazenamento simples
- **Datetime** para controle temporal

## Como Funciona <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Desktop%20Computer.png" alt="Computer" width="25" height="25" />

1. **Registro:**
   - Seleção do tipo de material em lista padronizada
   - Inserção de peso em quilogramas
   - Cálculo automático do valor total

2. **Armazenamento:**
   - Dados salvos em CSV com timestamp
   - Estrutura otimizada para análise

3. **Relatórios:**
   - Geração automática de CSVs diários/mensais
   - Download direto pela interface

4. **Análise:**
   - Visualização em tabelas e gráficos
   - Identificação de materiais mais reciclados
   - Cálculo de valores totais e médias

## Como Executar <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Play%20Button.png" alt="Play Button" width="25" height="25" />

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/recicla-mais.git
   ```

2. Instale as dependências:
   ```bash
   pip install streamlit pandas
   ```

3. Execute o sistema:
   ```bash
   streamlit run sistema_reciclagem.py
   ```

4. Acesse no navegador:
   ```
   http://localhost:8501
   ```

## Acesso Mobile <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Mobile%20Phone.png" alt="Mobile Phone" width="25" height="25" />
1. **Na mesma rede:**
   - Descubra o IP do computador (`ipconfig`)
   - Acesse `http://<IP-DO-PC>:8501` no celular

2. **Via internet:**
   - Use **ngrok** para criar um túnel:
     ```bash
     ngrok http 8501
     ```
   - Ou faça deploy no Streamlit Cloud

## Exemplo de Saída <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bar%20Chart.png" alt="Chart" width="25" height="25" />

- **Relatório CSV:**
  ```csv
  data,tipo,quantidade_kg,valor_por_kg,valor_total
  2023-11-15 14:30:00,Plastico,50.0,0.75,37.5
  ```

- **Dashboard:**
  ![Dashboard Preview](https://via.placeholder.com/800x400?text=Recicla+Dashboard+Preview)

## Estrutura do Projeto <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/File%20Folder.png" alt="Folder" width="25" height="25" />

```
recicla-mais/
├── sistema_reciclagem.py  # Código principal
├── registros_reciclagem.csv  # Dados armazenados
├── relatorios/            # Pasta de relatórios
├── README.md              # Este arquivo
└── requirements.txt       # Dependências
```

## Licença <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Copyright.png" alt="Copyright" width="25" height="25" />

MIT License - Consulte [LICENSE](LICENSE) para detalhes.

---

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" alt="Handshake" width="25" height="25" /> **Contribuições são bem-vindas!** Reporte issues ou envie pull requests.
