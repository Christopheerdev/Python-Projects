# Python-Projects

Projetos pessoais com aprendizado em Python

---

# 🚗 Sistema de Estacionamento em Python

Este projeto é um **sistema de estacionamento em Python**, desenvolvido com foco em prática de lógica e evolução para **Programação Orientada a Objetos (POO)**.

O sistema permite gerenciar veículos de diferentes categorias, registrar entradas e saídas e consultar informações de forma simples.

---

## 🧠 Conceitos Aplicados

Este projeto evoluiu de uma abordagem procedural para uma versão utilizando **POO**, incluindo:

* Programação Orientada a Objetos (POO)
* Herança (`Veiculo → Morador / Inquilino / Visitante`)
* Polimorfismo (métodos diferentes para cada tipo)
* Encapsulamento básico
* Estruturas condicionais (`if/elif/else`)
* Funções
* Loops (`while`)
* Manipulação de dados
* Registro de horários com `datetime`

---

## 📌 Funcionalidades

### ✅ Cadastro de veículos

O usuário pode cadastrar uma placa em três categorias:

* **Morador**
* **Inquilino (mensalista)**
* **Visitante (diária)**

---

### ✅ Identificação automática

O sistema identifica o tipo do veículo com base na placa cadastrada:

* Morador
* Inquilino
* Visitante
* Ou não cadastrado

---

### ✅ Controle de visitantes

Para visitantes, o sistema:

* Registra automaticamente o horário de entrada
* Permite registrar o horário de saída
* Calcula o valor da diária (R$ 20,00)
* Mantém um histórico completo

---

### ✅ Consulta de veículos

Permite consultar qualquer placa e visualizar suas informações.

---

### ✅ Histórico de visitantes

Lista todos os visitantes com:

* Placa
* Horário de entrada
* Horário de saída
* Valor pago

---

## 🏗️ Estrutura do Projeto

O sistema foi estruturado utilizando herança:

```
Veiculo (classe base)
│
├── Morador
├── Inquilino
└── Visitante
```

Cada tipo de veículo possui comportamentos específicos, como controle de entrada e saída no caso dos visitantes.

---

## 💡 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

* Consolidar conceitos de lógica de programação
* Praticar Programação Orientada a Objetos
* Simular um sistema real de controle de estacionamento
* Servir como projeto de portfólio para oportunidades na área de tecnologia

---

## 🚀 Possíveis Melhorias

* Persistência de dados (arquivos ou banco de dados)
* Interface gráfica (Tkinter ou web)
* Cálculo por tempo (horas em vez de diária fixa)
* Sistema de autenticação (admin / operador)

---

## 📎 Como executar

```bash
sistema_estacionamento.py
```

---

## 👨‍💻 Autor

Projeto desenvolvido por Christopher Garcia como parte dos estudos em Python e desenvolvimento de software.

