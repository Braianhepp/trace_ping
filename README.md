# Monitor de Dispositivos em Rede

## 📋 Descrição
Um sistema de monitoramento de dispositivos em rede desenvolvido em Python, que permite acompanhar em tempo real o status de múltiplos endereços IP através de uma interface gráfica moderna e intuitiva.

![image](https://github.com/user-attachments/assets/5ab86ee6-67da-4222-b0e5-2a9902d7fcf8)

![image](https://github.com/user-attachments/assets/00c138b0-a71f-48f5-a175-b99df4c5dba5)


## 🚀 Funcionalidades Principais

### 1. Monitoramento em Tempo Real
- Verificação contínua do status de dispositivos através de ping
- Atualização automática a cada segundo
- Indicação visual de status (Online/Offline)
- Registro de data e hora da última verificação

### 2. Gerenciamento de Dispositivos
- Adição de novos dispositivos com descrição personalizada
- Remoção de dispositivos do monitoramento
- Interface intuitiva para gerenciamento
- Persistência de dados em banco SQLite

### 3. Histórico de Eventos
- Registro detalhado de mudanças de estado
- Acompanhamento de duração de períodos offline
- Visualização dos últimos 100 eventos por dispositivo
- Timestamps precisos para cada evento

### 4. Interface Gráfica
- Design moderno com Tailwind CSS
- Interface responsiva e adaptável
- Tema escuro para melhor visualização
- Animações suaves para melhor experiência do usuário
- Modal para visualização detalhada do histórico
- Scrollbars personalizadas para melhor navegação

### 5. Armazenamento de Dados
- Banco de dados SQLite para persistência
- Registro de eventos históricos
- Armazenamento de configurações de dispositivos
- Recuperação automática dos dispositivos monitorados após reinicialização

### 6. Monitoramento Multithreading
- Monitoramento simultâneo de múltiplos dispositivos
- Threads independentes para cada dispositivo
- Gerenciamento eficiente de recursos
- Parada segura de threads ao remover dispositivos

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Flask (Framework Web)
- PyWebView (Interface Desktop)
- SQLite3 (Banco de Dados)
- Ping3 (Verificação de conectividade)
- Tailwind CSS (Estilização)
- JavaScript (Interatividade frontend)

## 📦 Requisitos
- Python 3.x
- Bibliotecas Python conforme requirements.txt:
  - ping3==4.0.3
  - pywebview==4.4.1
  - flask==3.0.2
  - ttkbootstrap==1.10.1
  - pillow==10.2.0

## 🚀 Como Executar
1. Clone o repositório
2. Instale as dependências:
3. pip install -r requirements.txt
4. Execute o arquivo principal:
5. python monitor_ip.py

## 💡 Recursos Adicionais
- Suporte a múltiplos sistemas operacionais
- Interface desktop nativa através do PyWebView
- Design responsivo para diferentes tamanhos de tela
- Sistema de notificação visual para mudanças de estado
- Gerenciamento eficiente de memória e recursos

## 🔍 Casos de Uso
- Monitoramento de servidores
- Acompanhamento de dispositivos IoT
- Supervisão de equipamentos de rede
- Monitoramento de infraestrutura de TI
- Diagnóstico de problemas de conectividade

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📄 Licença
Este projeto está sob a licença MIT.

## 👨‍💻 Autor
Desenvolvido por Braian Hepp
