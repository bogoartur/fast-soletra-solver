# 📝 **Fast Soletra Solver**  
Automatize sua performance no jogo **Soletra** do G1 com este script!  
Este projeto usa **Python** e a biblioteca **Selenium** para identificar rapidamente palavras válidas e inseri-las automaticamente no jogo.

---

## 🚀 **O que este script faz?**
1. 🕹️ **Joga o Soletra automaticamente**: Identifica as letras centrais e opcionais do jogo e usa uma lista de palavras para encontrar combinações válidas.
2. 📖 **Filtra palavras**:
   - Apenas palavras que atendem às regras do jogo (contêm a letra central e não usam letras proibidas).
   - Remove palavras repetidas e irrelevantes.
3. 🔄 **Atualiza listas de palavras**:
   - Adiciona novas palavras aprendidas ao longo do tempo.
   - Mantém um banco de dados atualizado de palavras com e sem acentos.

---

## 🛠️ **Como funciona?**
1. Abre o site [G1 Soletra](https://g1.globo.com/jogos/soletra/).
2. Identifica as letras principais na interface do jogo.
3. Usa listas predefinidas (`todasPalavrasSemAcento.txt`, `verbosConjugados.txt`) para calcular as palavras possíveis.
4. Digita automaticamente as palavras no jogo e limpa o campo para a próxima tentativa.

---

## 🧑‍💻 **Como usar**
1. Certifique-se de ter o **Python 3.x** instalado.
2. Instale as dependências:
   ```bash
   pip install selenium
3. Baixe o geckodriver (se estiver usando Firefox) e coloque-o no PATH.
4. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/fast-soletra-solver.git
5. Execute o script:
   ```bash
   python removendoConjugados.py
   
## 📊 **Histórico de Performance**
| **Data**   | **Palavras Encontradas** | **Tempo Levado** |
|------------|---------------------------|------------------|
| **07/12**  | 59/59                    | 55s 🏆           |
| **08/12**  | 76/91                    | 1m25s 🚀           |

---

## 🔍 **Como contribuo?**
- Adicione novas listas de palavras ou otimize o código para melhorar a performance.
- Relate bugs ou melhorias abrindo uma **issue** neste repositório.

---

## ⚠️ **Avisos**
- Este script é para fins educativos e pessoais. Não abuse do uso em sites que não autorizam automação.
- Testado com **Firefox** e Selenium. Pode exigir adaptações para outros navegadores.

---

## ✨ **Contribuidores**
- [Artur Bogo](https://github.com/bogoartur)  

Divirta-se jogando e vencendo! 🎉
