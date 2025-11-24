# Python-Projects
Projetos pessoais  com aprendizado de Python

# 🚗 Sistema de Estacionamento em Python

Este projeto é um **sistema de estacionamento simples**, desenvolvido em Python, ideal para estudo e para demonstrar conhecimentos de:

- Estruturas condicionais (`if/elif/else`)
- Funções
- Loops (`while`)
- Manipulação de dicionários
- Registro de horários com `datetime`
- Organização de código para portfólio

O sistema permite cadastrar placas, identificar o tipo de usuário, registrar entrada e saída de visitantes e calcular o valor da diária.

---

## 📌 Funcionalidades

### ✅ Cadastro de placas
O usuário pode cadastrar uma placa em três categorias:
- **Morador**
- **Inquilino** (mensalista)
- **Visitante** (diária)

### ✅ Identificação automática
O sistema identifica se a placa cadastrada é:
- Morador  
- Inquilino  
- Visitante  
- Ou se não está cadastrada  

### ✅ Visitantes
Para visitantes, o sistema:
- Registra **automáticamente o horário de entrada**
- Permite registrar **horário de saída**
- Calcula o valor da diária (R$ 20,00)
- Mantém um **histórico completo**

### ✅ Consultas
Você pode consultar qualquer placa a qualquer momento.

### ✅ Histórico de visitantes
Mostra todos os visitantes, com:
- Placa  
- Horário de entrada  
- Horário de saída  
- Valor pago  

---

## 🧠 Lógica Utilizada

- Moradores e inquilinos são armazenados em dicionários simples (`True` como valor).
- Visitantes são armazenados com:
```python
{
    "ABC1234": {
        "entrada": datetime,
        "saida": datetime,
        "valor": float
    }
}
