# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para o projeto **Conversação por Voz com ChatGPT**! 

## Como Contribuir

### Reportando Bugs

Se você encontrar um bug, por favor:

1. Verifique se o bug já não foi reportado nas [Issues](https://github.com/celloweb-ai/chatgpt-voice-conversation/issues)
2. Abra uma nova issue com:
   - Título descritivo
   - Passos para reproduzir o problema
   - Comportamento esperado vs comportamento atual
   - Screenshots (se aplicável)
   - Ambiente (OS, versão do Python, etc.)

### Sugerindo Melhorias

Sugestões são sempre bem-vindas! Para propor uma melhoria:

1. Abra uma issue com a tag `enhancement`
2. Descreva claramente a melhoria proposta
3. Explique por que ela seria útil

### Pull Requests

1. **Fork o repositório**

2. **Clone seu fork:**
   ```bash
   git clone https://github.com/seu-usuario/chatgpt-voice-conversation.git
   cd chatgpt-voice-conversation
   ```

3. **Crie uma branch para sua feature:**
   ```bash
   git checkout -b feature/minha-feature
   ```

4. **Faça suas alterações:**
   - Mantenha o código limpo e bem documentado
   - Siga as convenções de código Python (PEP 8)
   - Adicione comentários quando necessário
   - Teste suas alterações

5. **Commit suas mudanças:**
   ```bash
   git add .
   git commit -m "feat: adiciona nova funcionalidade X"
   ```

   **Convenções de commit:**
   - `feat:` Nova funcionalidade
   - `fix:` Correção de bug
   - `docs:` Mudanças na documentação
   - `style:` Formatação, espaços, etc.
   - `refactor:` Refatoração de código
   - `test:` Adição ou modificação de testes
   - `chore:` Atualizações de build, configurações, etc.

6. **Push para seu fork:**
   ```bash
   git push origin feature/minha-feature
   ```

7. **Abra um Pull Request:**
   - Descreva suas mudanças em detalhes
   - Referencie issues relacionadas
   - Aguarde o review

## Padrões de Código

### Python

- Siga o [PEP 8](https://pep8.org/)
- Use type hints quando possível
- Docstrings para funções e classes
- Máximo de 100 caracteres por linha

### Exemplo:

```python
def minha_funcao(parametro: str) -> dict:
    """
    Descrição breve da função.
    
    Args:
        parametro: Descrição do parâmetro
    
    Returns:
        Descrição do retorno
    """
    return {"resultado": parametro}
```

## Testes

Antes de submeter um PR:

1. Teste manualmente todas as funcionalidades afetadas
2. Verifique se não há erros no console
3. Teste em diferentes ambientes (se possível)

## Documentação

Se sua contribuição adicionar ou modificar funcionalidades:

- Atualize o README.md
- Adicione comentários no código
- Crie exemplos de uso, se aplicável

## Código de Conduta

- Seja respeitoso com todos os contribuidores
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros da comunidade

## Dúvidas?

Se tiver dúvidas sobre como contribuir:

- Abra uma issue com a tag `question`
- Entre em contato via GitHub

---

**Obrigado por contribuir! 🚀**
